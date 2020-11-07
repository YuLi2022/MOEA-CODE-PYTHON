"""
随机初始化种群 
"""
import numpy as np 

def initPops(nPop, nChr, lb, rb, Vmax, Vmin):
    pops = np.random.rand(nPop, nChr)*(rb-lb) + lb 
    VPops = np.random.rand(nPop, nChr)*(Vmax-Vmin) + Vmin
    return pops, VPops 