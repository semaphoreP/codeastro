"""
A script to test some edge cases for the calc_orbit() function. We threw a bunch of weird inputs in
and now everything is returning nans. Try to figure out which input or inputs is causing it to return nan.
If you have time, update the code to do some error checking to alert the user the input is invalid. 
"""
import numpy as np
import orbitize.kepler as kepler

ra, dec, rv = kepler.calc_orbit(np.array([1000, 1e6, -12]), 10.0, 0.1, -1, 1000, 0, 0.5, 100, -99)

print(ra, dec, rv)
assert np.all(np.isfinite(ra))
assert np.all(np.isfinite(dec))
assert np.all(np.isfinite(rv))