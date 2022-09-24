import numpy as np


def ElemSize(x):
    n = len(x)
    q = np.arange()
    s = np.zeros(n)
    for i in range(n):
        s[i] = (x[q[2, i], 1] - x[q[1, i], 1]) ** 2 + (x[q[2, i], 2] - x[q[1, i], 2]) ** 2

    h = np.sqrt(max(s))

    return h
