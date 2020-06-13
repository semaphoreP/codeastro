import matplotlib.pyplot as plt
import orbitize.driver

myDriver = orbitize.driver.Driver("broken_repo.csv", 'OFTI', 1, 1.22, 56.95, mass_err=0.08, plx_err=0.26)

s = myDriver.sampler
s.run_sampler(1000)

# test orbit plot generation
s.results.plot_orbits(start_mjd=myDriver.system.data_table['epoch'][0])
plt.show()