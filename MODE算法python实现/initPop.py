"""
初始化种群 
"""
import numpy as np 

def initPop(nChr, nPop, lb, rb):
    pops = np.ones((nPop,nChr)) * lb + \
         np.random.rand(nPop,nChr) * (rb - lb) 
    return pops  