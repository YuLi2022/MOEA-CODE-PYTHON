"""
更新archive集
"""
import numpy as np 

def getNonDominationPops(pops, fits): 
    """快速得到非支配解集 
    Params:
        pops: 种群，nPop * nChr 数组
        fits: 适应度， nPop * nF 数组 
    Return: 
        ranks: 每个个体所对应的等级，一维数组 
    """
    nPop = pops.shape[0] 
    nF = fits.shape[1]  # 目标函数的个数 
    ranks = np.ones(nPop, dtype=np.int32)  
    nPs = np.zeros(nPop)  # 每个个体p被支配解的个数 
    for i in range(nPop): 
        for j in range(nPop):
            if i == j:
                continue
            isDom1 = fits[i] <= fits[j] 
            isDom2 = fits[i] < fits[j] 
            # 是否被支配-> i被j支配 
            if sum(~isDom2) == nF and sum(~isDom1) >= 1:
                nPs[i] += 1 
    r = 0  # 当前等级为 0， 等级越低越好 
    indices = np.arange(nPop) 
    rIdices = indices[nPs==0]  # 当前被支配数为0的索引 
    ranks[rIdices] = 0  
    return pops[ranks==0], fits[ranks==0]  

def updateArchive(pops, fits, archive, arFits):
    """根据当前新的种群更新archive
    Return:
        newArchive
        newArFit
    """
    # 获取当前种群的非支配解
    nonDomPops, nonDomFits = getNonDominationPops(pops, fits) 
    isCh = np.zeros(nonDomPops.shape[0]) >= 1  # 开始全部设置为false
    nF = fits.shape[1]  # 目标个数 
    for i in range(nonDomPops.shape[0]): 
        # 判断arFits中是否有解支配当前种群的非支配解
        isDom1 = nonDomFits[i] >= arFits 
        isDom2 = nonDomFits[i] > arFits 
        isDom = (np.sum(isDom1, axis=1)==nF) & (np.sum(isDom2, axis=1)>=1) 
        if np.sum(~isDom) >= 1:
            # 说明archive集中没有一个解可以支配该解，那么将其添加进去
            isCh[i] = True  # 设置为可供选择 
    # 如果有支配解产生 
    if np.sum(isCh) >= 1:
        archive = np.concatenate((archive,nonDomPops[isCh]), axis=0) 
        arFits = np.concatenate((arFits, nonDomFits[isCh]), axis=0) 
    return archive, arFits 

        



