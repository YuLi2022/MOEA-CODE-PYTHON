"""
种群的合并和优选 
"""
import numpy as np 
from nonDominationSort import * 

def optSelect(pops, fits, chrPops, chrFits):
    """种群合并与优选 
    Return: 
        newPops, newFits 
    """
    nPop, nChr = pops.shape 
    nF = fits.shape[1] 
    newPops = np.zeros((nPop, nChr)) 
    newFits = np.zeros((nPop, nF)) 
    # 合并父代种群和子代种群构成一个新种群 
    MergePops = np.concatenate((pops,chrPops), axis=0) 
    MergeFits = np.concatenate((fits,chrFits), axis=0) 
    MergeRanks = nonDominationSort(MergePops, MergeFits) 
    MergeDistances = crowdingDistanceSort(MergePops, MergeFits, MergeRanks) 

    indices = np.arange(MergePops.shape[0]) 
    r = 0 
    i = 0 
    rIndices = indices[MergeRanks==r]  # 当前等级为r的索引 
    while i + len(rIndices)  <= nPop:
        newPops[i:i+len(rIndices)] = MergePops[rIndices] 
        newFits[i:i+len(rIndices)] = MergeFits[rIndices] 
        r += 1  # 当前等级+1 
        i += len(rIndices) 
        rIndices = indices[MergeRanks==r]  # 当前等级为r的索引 
    
    if i < nPop: 
        rDistances = MergeDistances[rIndices]   # 当前等级个体的拥挤度 
        rSortedIdx = np.argsort(rDistances)[::-1]  # 按照距离排序 由大到小 
        surIndices = rIndices[rSortedIdx[:(nPop-i)]]  
        newPops[i:] = MergePops[surIndices] 
        newFits[i:] = MergeFits[surIndices] 
    return (newPops, newFits) 
        

        






        