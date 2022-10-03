import numpy as np

def mesh_layers_t3(xlim, Y, N, h0):
    """

    Parameters
    ----------
    xlim - limits of rectangular domain on the x-axis
    Y - vector of layer interfaces; number of layers = len(Y)-1
    N - vector of layer refinements (x-times layer is finer)
    h0 - reference element size (N acts on h0 to get h_finer)

    Returns
    -------
    coord - Nodal coordinates
    lnod - element topology
    bound - boundary nodes (edges: bottom, right, top, left)
    elphz - enumerated layers
    """

    coord = []
    lnods = []
    elphz = []

    L = xlim[1] - xlim[0]
    H = Y[-1] - Y[0]
    nx0 = round(L / h0)

    nx = nx0 * 2 ** N[0]
    hx = L / nx
    dY = Y[1] - Y[0]

    if N[1] > N[0]:
        f = 2 * (1 - 1 / 2 ** (N[1] - N[0]))
        dy = dY / round(dY / (hx * np.sqrt(3) * 0.5)) * f
        dY = dY - dy
        # TODO Create meshRect_t3 function
        # labels: enhancement
        # assignees: iammix
        # milestone: v0.1.0_rc1
        coords, lnods = meshRect_t3(xlim, [Y[0], Y[1] - dy], hx)
        # TODO Create stepDown_t3 function
        # labels: enhancement
        # assignees: iammix
        # milestone: v0.1.0_rc1
        c, l = stepDown_t3(xlim, [Y[1] - dy, Y[1]], nx + 1, N[1] - N[0] + 1)


