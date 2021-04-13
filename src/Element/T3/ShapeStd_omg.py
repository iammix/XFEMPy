import numpy as np
from src.Shapes import LgBasis_tri


def ShapesStd_omg(nGauss, mGsPnt):
    nElNod = 3
    nDimes = 2
    mGsShp = np.zeros((nGauss, nElNod))
    mGsDrv = np.zeros((nDimes * nGauss, nElNod))

    jGsDrv = np.zeros(2)
    jGsDrv[0] = 1
    jGsDrv[1] = nDimes

    for iGauss in range(nGauss):
        mGsShp[iGauss, :], mGsDrv[jGsDrv[0]:jGsDrv[1], :] = LgBasis_tri(mGsPnt[iGauss, :], nElNod)
        jGsDrv[0] += nDimes
        jGsDrv[1] += nDimes

    return mGsShp, mGsDrv
