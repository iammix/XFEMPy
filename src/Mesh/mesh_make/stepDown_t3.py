import numpy as np


def stepDown_t3(xlim, ylim, nx, ny):
    l = xlim[1] - xlim[0]
    d = ylim[1] - ylim[0]
    hx = 1 / (nx - 1)
    hy = d / (2 - 1 / 2 ** (ny - 2))
    lnods = []
    coord = []
    for j in range(ny-1):
        if j > 0:
            ne = len(lnods)
            nn = len(coord) - nx
        else:
            ne = 0
            nn = 0
        lnods = [lnods, np.zeros(3*(nx-1), 3)]
    for i in range(nx-1):
        k = ne + 3*(i-1)
        n1 = nn + i
        n2 = n1 + 1
        n3 = nn + nx +(i-1)*2 +1
        n4 = n3 + 1
        n5 = n4 + 1

        lnods[k+1][0], lnods[k+1][1], lnods[k+1][2] = n1, n4, n3