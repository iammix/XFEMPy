import numpy as np

def LgWeight(N, a, b):
    """
    This script is for computing definite integrals using Legendre-Gauss
    Quadrature. Computes the Legendre-Gauss nodes and weights  on an interval
    [a,b] with truncation order N
    Suppose you have a continuous function f(x) which is defined on [a,b]
    which you can evaluate at any x in [a,b]. Simply evaluate it at all of
    the values contained in the x vector to obtain a vector f. Then compute
    the definite integral using sum(f.*w);
    """

    N1 = N
    N2 = N + 1
    N = N - 1
    xu = np.linspace(-1, 1, N1)

    # Initial Guess
    y = np.cos((2*(0:N)'+1)*pi/(2*N+2))+(0.27/N1)*sin(pi*xu*N/N2);