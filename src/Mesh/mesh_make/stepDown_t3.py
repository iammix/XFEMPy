import numpy as np


def stepDown_t3(xlim, ylim, nx, ny):
    l = xlim[1] - xlim[0]
    d = ylim[1] - ylim[0]
    hx = 1 / (nx - 1)
    hy = d / (2 - 1 / 2 ** (ny - 2))
    lnods = []
    coord = []
    for j in 
