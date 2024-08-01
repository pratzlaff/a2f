from astropy.io import fits
import numpy as np
import sys

x, y, d = np.loadtxt(sys.stdin, unpack=True)
hdu = fits.PrimaryHDU(d.reshape(int(y.max()), int(x.max())))
hdulist = fits.HDUList([hdu])
hdulist.writeto(sys.stdout.buffer)
