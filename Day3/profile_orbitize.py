"""
Let's profile the performance of orbitize! This will just allow us to asses the performance of some basic orbitize! functionality.

To profile this code, run the following command from the command line:

python -m cProfile -o profiler_output.txt profile_orbitize.py

The `-m cProfile` will attach the cProfile profiler to this script when it runs
The `-o profiler_output.txt` will save its output to "profiler_output.txt". 

If you have any issues running the above command, your python configuration might be different than what
we are assuing here. Ask a TA to help you figure out what needs to be changed if needed!

Note on parallelized code:
orbitize! by default is parallelized, but we will avoid doing that here. 
Using parallelism will make the cprofiler output more confusing than necessary. We just want to know what takes the most time,
summed up across multiple processes. Doing this on parallelized code, each process must save its own cProfile output and you 
need to combine the outputs afterwards (using `pstats.add()`). It is bset to avoid this when possible. Here, we do a very short 
orbit fit (probably not good enough for science) to benchmark our code on a single core in a short amount of time. 

"""


import orbitize
from orbitize import driver


myDriver = driver.Driver(
    '{}/GJ504.csv'.format(orbitize.DATADIR), # data file
    'OFTI',        # choose from: ['OFTI', 'MCMC']
    1,             # number of planets in system
    1.22,          # total system mass [M_sun]
    56.95,         # system parallax [mas]
    mass_err=0.08, # mass error [M_sun]
    plx_err=0.26   # parallax error [mas]
)
orbits = myDriver.sampler.run_sampler(1000,  num_cores=1)