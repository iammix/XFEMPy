import numpy as np

def StepUp_t3(xlim, ylim, nx, ny):
    """
    Generate a step-up triangular mesh with type 3 elements.

    Parameters:
        xlim (tuple): Limits of the rectangular domain on the x-axis.
        ylim (tuple): Limits of the rectangular domain on the y-axis.
        nx (int): Number of nodes along the x-axis.
        ny (int): Number of layers (number of times to step up).

    Returns:
        tuple: A tuple (coord, lnods, nx) containing the mesh information:
            coord (ndarray): Nodal coordinates.
            lnods (ndarray): Element topology.
            nx (int): Number of nodes on the x-axis for the next layer of elements.
    """
    l = xlim[1] - xlim[0]
    d = ylim[1] - ylim[0]

    hx = l / (nx - 1)  # initial size
    hy = d / (2**(ny - 1) - 1) / 2  # initial size (by geometric progression)

    lnods = []
    coord = []

    for j in range(1, ny):  # element row
        if j > 1:
            ne = lnods.shape[0]
            nn = coord.shape[0] - nx
        else:
            ne = 0
            nn = 0

        lnods = np.vstack((lnods, np.zeros((3 * (nx - 1) // 2, 3), dtype=int)))

        for i in range(1, (nx - 1) // 2 + 1):  # element pairs (column wise)
            k = ne + 3 * (i - 1)

            # node numbering
            # 4_____5
            # |\   /|
            # 1_\2/_3
            n1 = nn + (i - 1) * 2 + 1
            n2 = n1 + 1
            n3 = n2 + 1
            n4 = nn + nx + i
            n5 = n4 + 1

            lnods[k, :] = [n1, n2, n4]
            lnods[k + 1, :] = [n2, n5, n4]
            lnods[k + 2, :] = [n2, n3, n5]

        if j > 1:
            ylim = (ylim[0] + hy,) + ylim[1:]  # advance the y-reference datum
            coord = np.vstack((coord, np.column_stack((
                np.linspace(xlim[0], xlim[1], (nx - 1) // 2 + 1),
                np.full(((nx - 1) // 2 + 1,), ylim[0] + 2 * hy)))))
        else:
            coord = np.column_stack(
                np.hstack((np.linspace(xlim[0], xlim[1], nx),
                           np.linspace(xlim[0], xlim[1], (nx - 1) // 2 + 1))),
                np.vstack((np.full((nx,), ylim[0]), np.full(((nx - 1) // 2 + 1,), ylim[0] + 2 * hy)))).T

        hx *= 2
        hy *= 2

        nx = (nx - 1) // 2 + 1  # number of nodes on x-axis for the next layer of elements

    return coord, lnods, nx
