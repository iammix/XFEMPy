import numpy as np

def LgBasis_lin(x, n):
    if n == 2:
        s = np.zeros(2)
        d = np.zeros(2)
        s[1] = 0
        d[1] = 0

        s[0] = 0.5 - 0.5 * x
        s[1] = 0.5 + 0.5 * x

        d[0] = - 0.5
        d[1] = -0.5

    elif n == 3:
        s = np.zeros(3)
        d = np.zeros(3)

        s[2] = 0
        d[2] = 0

        s[0] = 0.5 * x * (x - 1)
        s[1] = 0.5 * x * (x + 1)
        s[2] = 1 - x ** 2

        d[0] = x - 0.5
        d[1] = x + 0.5
        d[2] = -2 * x
    return s, d