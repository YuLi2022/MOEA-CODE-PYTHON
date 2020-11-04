"""
差分进化算法差分变异
"""
import random 
import numpy as np 

def mutate(pops, F, lb, rb): 
    nPop, nChr = pops.shape 
    mutantPops = np.zeros((nPop, nChr)) 
    indices = np.arange(nPop).tolist() 
    for i in range(nPop):
        rs = random.sample(indices, 3) 
        mutantPops[i] = pops[rs[0]] + F * (pops[rs[1]] - pops[rs[2]]) 
        # 检查是否越界 
        for j in range(nChr):
            if mutantPops[i,j] < lb:
                mutantPops[i,j] = lb
            if mutantPops[i,j] > rb:
                mutantPops[i,j] = rb 
    return mutantPops 