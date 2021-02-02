"""Functions to perform correlations"""
import numpy as np
from scipy.stats import norm


def cross_corr(a, b):
    """Cross-correlation

    Calculate the cross correlation of array b against array a.

    Args:
        a (array): numpy vector. Reference against which cross
            correlation is calculated.
        b (array): numpy vector. The resulting cross-correlation function
            will show how b should be shifted to line up with vector a.

    Returns:
        array: cross-correlation function
    """
    # noramlize a & b
    a = (a-np.min(a))/(np.max(a)-np.min(a))
    b = (b-np.min(b))/(np.max(b)-np.min(b))

    # compute the Fast Fourrier Transform
    f_a = np.fft.fft(a)
    f_b = np.fft.fft(b)

    # get the complex conjugate
    f_a_c = np.conj(f_a)

    # Convolution Theorem: The Fourier transform of the convolution is
    # the product of the two Fourier transforms

    # Correlation theorem: multiplying the Fourier transform of
    # one function by the complex conjugate of the Fourier transform of
    # the other gives the Fourier transform of their correlation
    # The inverse then brings us back to the original domain
    c_corr = np.fft.ifft(f_a_c*f_b)

    # FFT cross corr method gives the cyclic cross-correlation
    # "first n points in c_corr[0..2*n] stored in wrap-around order,
    # i.e., correlations at increasingly negative lags are in c_corr[n]
    # on down to c_corr[n/2+1], while correlations at increasingly
    # positive lags are in c_corr[0] (zero lag) on up to c_corr[n/2]."
    # --> Numerical Recipes in C to get the linear correlation, need to
    # circularly rotate the data this puts the peaks of the signal
    # together
    c_corr = np.abs(np.roll(c_corr, len(c_corr) // 2))
    # above does the same as np.fft.fftshift
    # note that the shift occurs on a pixel/array element level,
    # so len/2 has to be an integer so enforce floor/int division here

    # normalizing, may help peak fitting
    c_corr = (c_corr-np.min(c_corr))/(np.max(c_corr)-np.min(c_corr))

    return c_corr


def find_shift(a, b):
    """Find offset between a and b.

    Find the offset between vector a and b that makes them line up as
    well as possible.

    Args:
        a (array): Reference vector
        b (array): Target vector

    Returns:
        float: the shift needed to be applied to vector b to
            best match vector a

    """
    npt = len(a)
    c_corr = cross_corr(a, b)

    # define the lag grid that corresponds to the cross-correlation
    lag_grid = np.arange(npt) - npt // 2

    # multiply by the pixel width to put in same units as the
    # original function
    x_lag = lag_grid*(x[1]-x[0])

    # the peak or center of the cross-correlation gives us the shift
    # between the arrays fit 2nd order poly to peak of cross-corr
    ind_c_max = np.where(c_corr == np.max(c_corr))[0]
    ind_c_max = ind_c_max[0]
    result = np.polyfit(x_lag[ind_c_max-2:ind_c_max+2],
                        c_corr[ind_c_max-2:ind_c_max+2], 2)

    # differentiate and set to zero to find peak
    shift_y2 = -result[1]/(2.*result[0])

    return shift_y2


if __name__ == '__main__':
    # generate x-axis grid
    x = (np.arange(100)-50.23)*3.67

    # generate Gaussian profile for that grid
    c1 = 2
    c2 = -17.3
    y1 = norm.pdf(x, c1, 7)
    y2 = norm.pdf(x, c2, 7)

    # do the cross-correlation
    shift = find_shift(y1, y2)

    print("Shift array b by {:.0f} pixels to line up with array a." \
          .format(shift))
