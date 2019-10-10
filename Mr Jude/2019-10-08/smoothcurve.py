import numpy as np

from scipy.interpolate import make_interp_spline


def make(x, data):
    xNP = np.array(x)
    xNew = np.linspace(xNP.min(), xNP.max(), 1000)
    dataNP = np.array(data)
    return xNew, (make_interp_spline(xNP, dataNP, k=3))(xNew)
