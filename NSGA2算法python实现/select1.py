"""
选择算子 
"""
import random 
import numpy as np 

def select1(pool, pops, fits, ranks, distances):
    # 一对一锦标赛选择 
    # pool: 新生成的种群大小 
    nPop, nChr = pops.shape 
    nF = fits.shape[1] 
    newPops = np.zeros((pool, nChr)) 
    newFits = np.zeros((pool, nF))  

    indices = np.arange(nPop).tolist()
    i = 0 
    while i < pool: 
        idx1, idx2 = random.sample(indices, 2)  # 随机挑选两个个体 
        idx = compare(idx1, idx2, ranks, distances) 
        newPops[i] = pops[idx] 
        newFits[i] = fits[idx] 
        i += 1 
    return newPops, newFits 


def compare(idx1, idx2, ranks, distances): 
    # return: 更优的 idx 
    if ranks[idx1] < ranks[idx2]: 
        idx = idx1 
    elif ranks[idx1] > ranks[idx2]:
        idx = idx2 
    else:
        if distances[idx1] <= distances[idx2]:
            idx = idx2 
        else:
            idx = idx1 
    return idx  

