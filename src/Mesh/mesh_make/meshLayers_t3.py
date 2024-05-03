import numpy as np
from mesh.mesh_make.meshRect_t3 import *

def meshLayers_t3(xlim, Y, N, h0):
    """
    Generate a layered triangular mesh with type 3 elements.

    Parameters:
        xlim (tuple): Limits of the rectangular domain on the x-axis.
        Y (list): Layer interfaces; the number of layers is len(Y)-1.
        N (list): Layer refinements (number of times each layer is finer).
        h0 (float): Reference element size.

    Returns:
        tuple: A tuple (coord, lnods, bound, elphz) containing the mesh information:
            coord (ndarray): Nodal coordinates.
            lnods (ndarray): Element topology.
            bound (list): Boundary nodes (edges: bottom, right, top, left).
            elphz (ndarray): Enumerated layers.
    """
    coord = np.empty((0, 2))  # (stacking on top)
    lnods = np.empty((0, 3), dtype=int)
    elphz = np.empty((0, 1), dtype=int)

    L = xlim[1] - xlim[0]
    H = Y[-1] - Y[0]

    nx0 = round(L / h0)

    # DO FIRST LAYER
    nx = nx0 * 2**N[0]
    hx = L / nx

    dY = Y[1] - Y[0]

    if N[1] > N[0]:  # with step-down
        f = 2 * (1 - 1 / 2**(N[1] - N[0]))  # (coarse to fine)
        dy = dY / round(dY / (hx * np.sqrt(3) * 0.5)) * f
        dY -= dy
        coord, lnods = MeshRect_t3(xlim, [Y[0], Y[1] - dy], hx)
        c, l = StepDown_t3(xlim, [Y[1] - dy, Y[1]], nx + 1, N[1] - N[0] + 1)
        c = c[nx + 1:, :]
        l += coord.shape[0] - nx - 1
        coord = np.concatenate((coord, c), axis=0)
        lnods = np.concatenate((lnods, l), axis=0)
    else:  # mesh until end of this layer
        coord, lnods = MeshRect_t3(xlim, [Y[0], Y[1]], hx)

    elphz = np.ones((lnods.shape[0], 1), dtype=int)

    # DO OTHER LAYERS (EXCEPT LAST)
    for i in range(1, len(N) - 1):
        dY = Y[i + 1] - Y[i]
        if N[i - 1] > N[i]:  # with step-up
            f = 2 * (2**(N[i - 1] - N[i]) - 1)  # (fine to coarse)
            dy = dY / round(dY / (hx * np.sqrt(3) * 0.5)) * f
            c, l = StepUp_t3(xlim, [Y[i], Y[i] + dy], nx + 1, N[i - 1] - N[i] + 1)
            c = c[nx + 1:, :]
            l += coord.shape[0] - nx - 1
            coord = np.concatenate((coord, c), axis=0)
            lnods = np.concatenate((lnods, l), axis=0)
            elphz = np.concatenate((elphz, i * np.ones((l.shape[0], 1), dtype=int)), axis=0)
            Y[i] += dy
            dY -= dy
        nx = nx0 * 2**N[i]
        hx = L / nx
        if N[i + 1] > N[i]:  # with step-down
            f = 2 * (1 - 1 / 2**(N[i + 1] - N[i]))  # (coarse to fine)
            dy = dY / round(dY / (hx * np.sqrt(3) * 0.5)) * f
            dY -= dy
            c, l = MeshRect_t3(xlim, [Y[i], Y[i + 1] - dy], hx)
            c = c[nx + 1:, :]
            l += coord.shape[0] - nx - 1
            coord = np.concatenate((coord, c), axis=0)
            lnods = np.concatenate((lnods, l), axis=0)
            elphz = np.concatenate((elphz, i * np.ones((l.shape[0], 1), dtype=int)), axis=0)
            c, l = StepDown_t3(xlim, [Y[i + 1] - dy, Y[i + 1]], nx + 1, N[i + 1] - N[i] + 1)
        else:  # mesh until end of this layer
            c, l = MeshRect_t3(xlim, [Y[i], Y[i + 1]], hx)
        c = c[nx + 1:, :]
        l += coord.shape[0] - nx - 1
        coord = np.concatenate((coord, c), axis=0)
        lnods = np.concatenate((lnods, l), axis=0)
        elphz = np.concatenate((elphz, i * np.ones((l.shape[0], 1), dtype=int)), axis=0)

    # DO LAST LAYERS
    i = len(N) - 1
    dY = Y[i + 1] - Y[i]
    if N[i - 1] > N[i]:  # step-up mesh size
        f = 2 * (2**(N[i - 1] - N[i]) - 1)  # (fine to coarse)
        dy = dY / round(dY / (hx * np.sqrt(3) * 0.5)) * f
        c, l = StepUp_t3(xlim, [Y[i], Y[i] + dy], nx + 1, N[i - 1] - N[i] + 1)
        c = c[nx + 1:, :]
        l += coord.shape[0] - nx - 1
        coord = np.concatenate((coord, c), axis=0)
        lnods = np.concatenate((lnods, l), axis=0)
        elphz = np.concatenate((elphz, i * np.ones((l.shape[0], 1), dtype=int)), axis=0)
        Y[i] += dy
        dY -= dy
    nx = nx0 * 2**N[i]
    hx = L / nx
    c, l = MeshRect_t3(xlim, [Y[i], Y[i + 1]], hx)
    c = c[nx + 1:, :]
    l += coord.shape[0] - nx - 1
    coord = np.concatenate((coord, c), axis=0)
    lnods = np.concatenate((lnods, l), axis=0)
    elphz = np.concatenate((elphz, i * np.ones((l.shape[0], 1), dtype=int)), axis=0)

    # GET DOMAIN BOUNDARY NODES
    bound = []
    tol = max(L, H) * 1e-12
    bound.append(np.where(np.abs(coord[:, 1] - min(coord[:, 1])) < tol)[0])
    bound.append(np.where(np.abs(coord[:, 0] - max(coord[:, 0])) < tol)[0])
    bound.append(np.where(np.abs(coord[:, 1] - max(coord[:, 1])) < tol)[0])
    bound.append(np.where(np.abs(coord[:, 0] - min(coord[:, 0])) < tol)[0])

    return coord, lnods, bound, elphz
