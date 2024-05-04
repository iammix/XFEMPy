import numpy as np

def MeshRect_t3(xlim, ylim, h0):
    """
    Generate a triangular mesh for a rectangular domain with triangle type 3 elements.

    Parameters:
        xlim (tuple): A tuple (xmin, xmax) defining the x-coordinate limits of the domain.
        ylim (tuple): A tuple (ymin, ymax) defining the y-coordinate limits of the domain.
        h0 (float): Characteristic element size.

    Returns:
        tuple: A tuple (p, t, b) containing the mesh information:
            p (ndarray): Node coordinates of shape (np, 2) where np is the number of nodes.
            t (ndarray): Element topology of shape (ne, 3) where ne is the number of elements.
            b (list): List of boundary node indices, b[0] to b[3] representing the four boundary segments.
    """
    L = xlim[1] - xlim[0]
    H = ylim[1] - ylim[0]

    nx = round(L / h0)
    ny = round(H / (h0 * np.sqrt(3) / 2))

    if ny - 2 * np.floor(ny / 2) == 1:
        ny = ny + 1  # make even

    np = (nx + 1) * (ny + 1) + ny // 2
    ne = (2 * nx + 1) * ny // 2

    p = np.zeros((np, 2))
    t = np.zeros((ne, 3))
    b = [None] * 4

    hx = L / nx
    hy = H / ny

    x1 = np.arange(xlim[0], xlim[1] + hx, hx)
    y1 = np.arange(ylim[0], ylim[1] + 2 * hy, 2 * hy)

    x2 = np.concatenate(([xlim[0]], x1[:-1] + hx / 2, [xlim[1]]))
    y2 = y1[:-1] + hy

    Tp = 2 * (nx + 1) + 1  # N points per layer
    Te = 2 * (2 * nx + 1)  # N elements per layer

    for i in range(1, ny // 2 + 1):  # go by period
        # node coordinates for this layer
        p[(i - 1) * Tp:i * Tp, 0] = np.tile(x1, 2)
        p[(i - 1) * Tp:i * Tp, 1] = np.tile(y1[i - 1], Tp)

        p[i * Tp - nx - 1:i * Tp, 0] = np.tile(x2, 2)
        p[i * Tp - nx - 1:i * Tp, 1] = np.tile(y2[i - 1], Tp)

        # element topology for this layer (right-angle triangles)
        t[(i - 1) * Te:i * Te:2, 0] = np.arange((i - 1) * Tp, i * Tp - nx - 1)
        t[(i - 1) * Te:i * Te:2, 1] = np.arange(i * Tp - nx, i * Tp - 1)
        t[(i - 1) * Te:i * Te:2, 2] = np.arange(i * Tp - nx - 1, i * Tp)

        t[(i - 1) * Te + 1:i * Te:2, 0] = np.arange(i * Tp - nx - 1, i * Tp + 1)
        t[(i - 1) * Te + 1:i * Te:2, 1] = np.arange(i * Tp - nx, i * Tp)
        t[(i - 1) * Te + 1:i * Te:2, 2] = np.arange(i * Tp - 1, i * Tp + nx + 1)

    # node coordinates for top boundary
    p[-nx:, 0] = x1
    p[-nx:, 1] = np.tile(y1[-1], nx + 1)

    # boundary nodes
    b[0] = np.arange(nx + 1)
    b[1] = np.where(p[:, 0] > xlim[1] - h0 / 4)[0]
    b[2] = np.arange(np - nx, np)
    b[3] = np.where(p[:, 0] < xlim[0] + h0 / 4)[0]

    return p, t, b
