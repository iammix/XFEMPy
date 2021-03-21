import numpy as np
from Gauss import LgWeight

def Gause_DomLin(nGauss):
    if nGauss == 1:
        vGsPnt = 0
        vGsWgt = 2
    elif nGauss == 2:
        vGsPnt =
    elif nGauss == 3:
        pass

    elif nGauss == 4:
        pass
    elif nGauss == 5:
        pass
    else:
        vGsPnt, vGsWgt = LgWeight(nGauss, -1, 1)