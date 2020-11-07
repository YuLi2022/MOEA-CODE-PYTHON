"""
更新个体最优集pBest
"""

import numpy as np 

def updatePBest(pBest, pFits, pops, fits):
    nPop, nF = fits.shape
    isDom1 = fits < pFits 
    isDom2 = fits <= pFits 
    isCh = (np.sum(isDom1, axis=1) == nF) & \
            (np.sum(isDom2, axis=1) >= 1) 
    if np.sum(isCh) >= 1:
        # 种群中的解支配pBest的话更新pBest
        pBest[isCh] = pops[isCh] 
        pFits[isCh] = fits[isCh] 
    return pBest, pFits 