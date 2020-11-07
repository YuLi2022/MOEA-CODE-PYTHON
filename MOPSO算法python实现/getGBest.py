"""
获取gBest
"""
from collections import Counter 
import random
from matplotlib.pyplot import axis 
import numpy as np

def getPosition(archive, arFits, M): 
    """获得当前archive集的位置 
    Params：
        archive: archive集
        arFits：对应的适应度
        M: 划分的网格大小为M*M 
    Return：
        flags: 每个粒子对应的位置, nF维映射为1位
    """
    fmin = np.min(arFits, axis=0) 
    fmax = np.max(arFits, axis=0) 
    grid = (fmax-fmin)/M  # 网格的长宽 
    pos = np.ceil((arFits-fmin)/grid)  
    nA, nF = pos.shape
    flags = np.zeros(nA) 
    for dim in range(nF-1):
        flags += (pos[:, dim] - 1) * (M**(nF-dim-1)) 
    flags += pos[:,-1] 
    return flags 

def getGBest(pops, fits, archive, arFits, M):
    # 根据密度来从archive集中选择gBest
    nPop, nChr = pops.shape 
    nF = fits.shape[1]
    gBest = np.zeros((nPop, nChr)) 
    flags = getPosition(archive, arFits, M)  
    # 统计每个网格出现的次数 
    counts = Counter(flags).most_common() 
    for i in range(nPop):
        # 首先从archive中寻找没有被pops[i]支配的集合
        isDom1 = fits[i] <= arFits 
        isDom2 = fits[i] < arFits 
        isDom = (np.sum(isDom1, axis=1)==nF) & \
            (np.sum(isDom2, axis=1)>=1) 
        # 之前的isDom是指pop[i]能够支配archive的集合，这里要取反
        isDom = ~isDom  
        if np.sum(isDom) == 0:
            gBest[i] = pops[i] 
            continue 
        elif np.sum(isDom) == 1:
            gBest[i] = archive[isDom] 
            continue 
        archivePop = archive[isDom]  
        #archivePopFit = arFits[isDom] 
        # 找出ai集中每个个体所处的位置 
        aDomFlags = flags[isDom]
        # 统计每个网格出现的次数 
        counts = Counter(aDomFlags).most_common() 
        minFlag, minCount = counts[-1]  # 出现次数最少的网格及其次数
        # 可能有多个网格的出现的次数相同，并且同样次数最小
        minFlags = [counts[i][0] for i in range(len(counts))
                    if counts[i][1]==minCount]  
        isCh = False 
        for minFlag in minFlags:
            isCh = isCh | (aDomFlags == minFlag) 
        indices = np.arange(aDomFlags.shape[0])  # 索引 
        chIndices = indices[isCh]
        # 从待选集中随机选择一个 
        idx = chIndices[int(np.random.rand()*len(chIndices))] 
        gBest[i] = archivePop[idx]  # 复制给相应的gBest位置上 
    return gBest 



        









             
            
        


