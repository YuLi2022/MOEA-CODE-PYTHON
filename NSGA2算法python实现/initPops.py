"""
种群初始化 
"""
import numpy as np 

def initPops(nPop, nChr, lb, rb): 
    pops = np.random.rand(nPop, nChr) * (rb - lb) + lb  
    return pops 
