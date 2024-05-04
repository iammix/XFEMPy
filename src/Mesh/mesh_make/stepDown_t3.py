import numpy as np

def stepDown_t3(xlim, ylim, nx, ny):
    """
    Generate a step-down triangular mesh with type 3 elements.

    Parameters:
        xlim (tuple): Limits of the rectangular domain on the x-axis.
        ylim (tuple): Limits of the rectangular domain on the y-axis.
        nx (int): Number of nodes along the x-axis.
        ny (int): Number of layers (number of times to step down).

    Returns:
        tuple: A tuple (coord, lnods, nx) containing the mesh information:
            coord (ndarray): Nodal coordinates.
            lnods (ndarray): Element topology.
            nx (int): Number of nodes on the x-axis for the next layer of elements.
    """
    l = xlim[1] - xlim[0]
    d = ylim[1] - ylim[0]

    hx = l / (nx - 1)  # initial size
    hy = d / (2 - 1 / 2**(ny - 2))  # initial size (by geometric progression)

    lnods = []
    coord = []

    for j in range(1, ny):  # element row
        if j > 1:
            ne = lnods.shape[0]
            nn = coord.shape[0] - nx
        else:
            ne = 0
            nn = 0

        lnods = np.vstack((lnods, np.zeros((3 * (nx - 1), 3), dtype=int)))

        for i in range(1, nx):  # element pairs (column wise)
            k = ne + 3 * (i - 1)  # element counter

            # node numbering
            # 3__4__5
            # | / \ |
            # 1/___\2
            n1 = nn + i
            n2 = n1 + 1
            n3 = nn + nx + (i - 1) * 2 + 1
            n4 = n3 + 1
            n5 = n4 + 1

            lnods[k, :] = [n1, n4, n3]
            lnods[k + 1, :] = [n1, n2, n4]
            lnods[k + 2, :] = [n2, n5, n4]

        if j > 1:
            ylim = (ylim[0] + 2 * hy,) + ylim[1:]  # advance the y-reference datum
            coord = np.vstack((coord, np.column_stack((
                np.linspace(xlim[0], xlim[1], 2 * nx - 1),
                np.full((2 * nx - 1,), ylim[0] + hy)))))
        else:
            coord = np.column_stack(
                np.hstack((np.linspace(xlim[0], xlim[1], nx),
                           np.linspace(xlim[0], xlim[1], 2 * nx - 1))),
                np.vstack((np.full((nx,), ylim[0]), np.full((2 * nx - 1,), ylim[0] + hy)))).T

        hx /= 2
        hy /= 2

        nx = 2 * nx - 1  # number of nodes on x-axis for the next layer of elements

    return coord, lnods, nx
