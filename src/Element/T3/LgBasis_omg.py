import numpy as np


def LgBasis_omg(p, n):
    x = p[0]
    y = p[1]

    if n == 3:
        s = np.zeros(3)
        d = np.zeros((2, 3))

        s[0] = 1 - x - y
        s[1] = x
        s[2] = y

        d[0, 0] = -1
        d[0, 1] = 1
        d[0, 2] = 0
        d[1, 0] = -1
        d[1, 1] = 0
        d[1, 2] = 1

    if n == 6:
        s = np.zeros(6)
        d = np.zeros((2, 6))

        s[0] = 1 - 3 * (x + y) + 2 * (x + y) ** 2
        s[1] = 4 * x * (1 - x - y)
        s[2] = x * (2 * x - 1)
        s[3] = 4 * x * y
        s[4] = y * (2 * y - 1)
        s[5] = 4 * y * (1 - x - y)

        d[0, 0] = 4 * (x + y) - 3
        d[0, 1] = 4 * (1 - 2 * x - y)
        d[0, 2] = 4 * x - 1
        d[0, 3] = 4 * y
        d[0, 4] = 0
        d[0, 5] = -4 * y
        d[1, 0] = 4 * (x + y) - 3
        d[1, 1] = -4 * x
        d[1, 2] = 0
        d[1, 3] = 4 * x
        d[1, 4] = 4 * y - 1
        d[1, 5] = 4 * (1 - x - 2 * y)


    return s, d
