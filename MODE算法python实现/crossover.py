"""
杂交算子
"""
from random import choices
import numpy as np 

def crossover(pops, mutantPops, Cr):
    nPop, nChr = pops.shape 
    choiMuPops1 = np.random.rand(nPop, nChr) < Cr  # 选择变异向量的位置1 
    choiMuPops2 = np.random.randint(0,nPop,(nPop,nChr))  == \
        np.tile(np.arange(nChr),(nPop,1))  # 选择变异向量的位置2 
    choiMuPops = choiMuPops1 | choiMuPops2 
    choiPops = ~ choiMuPops 
    trialPops = mutantPops * choiMuPops + pops * choiPops 
    return trialPops 


    
