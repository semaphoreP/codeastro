import time
import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt

Mtotal = 1000  # system mass [kg]
Npart = 1000   # number of particles
Mpart = Mtotal / Npart
radius = 1     # sphere radius [m]
Vcf = 0.5      # fraction of circular velocity
G = 6.673e-11  # gravitational constant

tstop = 1000  # stop time (seconds)
dt = 10.0

np.random.seed(12345)

# 
# 
def initialize(N):
    # Initialize a uniform distribution in a cube centered on the origin and then restrict to
    # sphere.  A cube that bounds a sphere has about twice the volume.  So to be on the safe
    # side (because randomness), I generate `3*Npart` particle positions and then select the
    # first `Npart` particles that lie within the sphere.
    ninside = 0
    while ninside < N:
        cubepos = 2*np.random.random([3*N,3]) - 1
        r = (cubepos**2).sum(1)**0.5
        inside = (r<1)
        ninside = inside.sum()
    pos = cubepos[inside][:N,:]
    r = (pos**2).sum(1)**0.5

    # Circular radius of a cross-section (xy-plane) of the sphere at coordinate z of the
    # particle. This is the particle's initial orbit for a solid body rotator. We need this to
    # calculate the x- and y-components of the initial velocity.
    rcirc = (pos[:,:2]**2).sum(1)**0.5
    vc = np.sqrt(G * Mtotal * r**2 / radius**3)
    
    vel = np.empty([N,3])
    vel[:,0] = -Vcf*vc * (pos[:,1] / rcirc)  # ratio is (y/r), which is sin(theta)
    vel[:,1] = +Vcf*vc * (pos[:,0] / rcirc)  # ratio is (x/r), which is cos(theta)
    vel[:,2] = 0.0
    
    return pos, vel

def subrange(comm):
    ### MODIFY HERE to determine the starting and ending point that an MPI process 
    ### will compute in the force calculation.
    size = comm.Get_size()  # Total number of processes
    rank = comm.Get_rank()  # Rank of the current process

    # Distribute the particles evenly across all processes accounting for non-divisible cases
    particles_per_process = Npart // size
    remainder = Npart % size

    if rank < remainder: #non-divisible case
        start = rank * (particles_per_process + 1)
        end = start + particles_per_process + 1
    else: # divisble case
        start = rank * particles_per_process + remainder
        end = start + particles_per_process
    return start, end, end-start

def calc_accel(comm, pos):
    start, end, Nsub = subrange(comm)

    # indices for when we include forces from all other particles
    idx = np.arange(Npart) 
    
    # acceleration for particles being calculated on this MPI process (core)
    accel = np.empty([Nsub,3])
    
    # only calculate acceleration for start -> end in the particle list
    for i in range(start,end):
        rij = pos[idx != i, :] - pos[i,:]  # exclude self (idx != i)
        rij_mag = (rij**2).sum(1)**0.5
        accel[i-start,:] = (rij / rij_mag[:,np.newaxis]**1.5).sum(0)
    
    # multiply by G*M at the very end
    accel *= G*Mpart
    
    ### MODIFY HERE to share the accelerations from each MPI process to 
    ### all other processes
    all_accel = np.empty([Npart, 3])
    comm.Allgather([accel, MPI.DOUBLE], [all_accel, MPI.DOUBLE])

    # all_accel = accel  # serial only (comment out after parallelized)
    return all_accel

def leapfrog_initialstep(comm, pos, vel, dt):
    accel = calc_accel(comm, pos)
    vhalf = vel + 0.5*dt * accel
    return vhalf

def leapfrog(comm, pos, vel, vhalf, dt):
    pos = pos + dt * vhalf
    anext = calc_accel(comm, pos)
    k = dt * anext
    # Only need v(t+dt) if we need to calculate associated quantities (e.g. energy) or plot it
    vel = vhalf + 0.5*k
    vhalf = vhalf + k
    return pos, vel, vhalf

#######################
#######################
#######################

comm = MPI.COMM_WORLD
if comm.rank == 0:
    pos, vel = initialize(Npart)
else:
    pos, vel = None, None

# MODIFY HERE to share the initial conditions that were only generated on the root (rank-0)
# process with the other MPI processes
pos, vel = comm.bcast((pos, vel), root=0)

vhalf = leapfrog_initialstep(comm, pos, vel, dt)
istep = 0
_time = 0.0
nstep = tstop/dt
time0 = time.perf_counter()
while _time < tstop:
    pos, vel, vhalf = leapfrog(comm, pos, vel, vhalf, dt)
    istep += 1
    _time += dt
    if (comm.rank == 0) and (istep % (nstep/10) == 0 or istep == 1):
        plt.clf()
        plt.scatter(pos[:,1], pos[:,2], s=10, c=np.linspace(0,1,Npart), cmap='coolwarm')
        plt.title(f"Time = {_time:.0f} s")
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.savefig(f"positions-{istep:04d}.png")
        print(f"time = {_time:.0f}/{tstop:.0f} seconds")
time1 = time.perf_counter()
telapsed = time1-time0
if comm.rank == 0:
    print(f"Compute time elapsed = {telapsed:.3f} seconds ({nstep/telapsed:.1f} steps/sec // {Npart*nstep/telapsed:.3g} particle-evolve/sec)")
