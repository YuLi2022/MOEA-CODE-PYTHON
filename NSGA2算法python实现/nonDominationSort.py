"""
快速非支配排序 
"""
import random 
import numpy as np

def nonDominationSort(pops, fits): 
    """快速非支配排序算法
    Params:
        pops: 种群，nPop * nChr 数组
        fits: 适应度， nPop * nF 数组 
    Return: 
        ranks: 每个个体所对应的等级，一维数组 
    """
    nPop = pops.shape[0] 
    nF = fits.shape[1]  # 目标函数的个数 
    ranks = np.zeros(nPop, dtype=np.int32)  
    nPs = np.zeros(nPop)  # 每个个体p被支配解的个数 
    sPs = []  # 每个个体支配的解的集合，把索引放进去 
    for i in range(nPop): 
        iSet = []  # 解i的支配解集 
        for j in range(nPop):
            if i == j:
                continue
            isDom1 = fits[i] <= fits[j] 
            isDom2 = fits[i] < fits[j] 
            # 是否支配该解-> i支配j
            if sum(isDom1) == nF and sum(isDom2) >= 1:
                iSet.append(j) 
            # 是否被支配-> i被j支配 
            if sum(~isDom2) == nF and sum(~isDom1) >= 1:
                nPs[i] += 1 
        sPs.append(iSet)  # 添加i支配的解的索引 
    r = 0  # 当前等级为 0， 等级越低越好 
    indices = np.arange(nPop) 
    while sum(nPs==0) != 0: 
        rIdices = indices[nPs==0]  # 当前被支配数为0的索引 
        ranks[rIdices] = r  
        for rIdx in rIdices:
            iSet = sPs[rIdx]  
            nPs[iSet] -= 1 
        nPs[rIdices] = -1  # 当前等级的被支配数设置为负数  
        r += 1 
    return ranks 


# 拥挤度排序算法 
def crowdingDistanceSort(pops, fits, ranks):
    """拥挤度排序算法
    Params:
        pops: 种群，nPop * nChr 数组
        fits: 适应度， nPop * nF 数组 
        ranks：每个个体对应的等级，一维数组 
    Return：
        dis: 每个个体的拥挤度，一维数组 
    """
    nPop = pops.shape[0] 
    nF = fits.shape[1]  # 目标个数 
    dis = np.zeros(nPop) 
    nR = ranks.max()  # 最大等级 
    indices = np.arange(nPop) 
    for r in range(nR+1):
        rIdices = indices[ranks==r]  # 当前等级种群的索引 
        rPops = pops[ranks==r]  # 当前等级的种群
        rFits = fits[ranks==r]  # 当前等级种群的适应度 
        rSortIdices = np.argsort(rFits, axis=0)  # 对纵向排序的索引 
        rSortFits = np.sort(rFits,axis=0) 
        fMax = np.max(rFits,axis=0) 
        fMin = np.min(rFits,axis=0) 
        n = len(rIdices)
        for i in range(nF): 
            orIdices = rIdices[rSortIdices[:,i]]  # 当前操作元素的原始位置 
            j = 1  
            while n > 2 and j < n-1:
                if fMax[i] != fMin[i]:
                    dis[orIdices[j]] += (rSortFits[j+1,i] - rSortFits[j-1,i]) / \
                        (fMax[i] - fMin[i]) 
                else:
                    dis[orIdices[j]] = np.inf 
                j += 1 
            dis[orIdices[0]] = np.inf 
            dis[orIdices[n-1]] = np.inf   
    return dis  



if __name__ == "__main__":
    y1 = np.arange(1,5).reshape(4,1)
    y2 = 5 - y1 
    fit1 = np.concatenate((y1,y2),axis=1) 
    y3 = 6 - y1 
    fit2 = np.concatenate((y1,y3),axis=1)
    y4 = 7 - y1 
    fit3 = np.concatenate((y1,y4),axis=1) 
    fit3 = fit3[:2] 
    fits = np.concatenate((fit1,fit2,fit3), axis=0) 
    pops = np.arange(fits.shape[0]).reshape(fits.shape[0],1) 

    
    random.seed(123)
    # 打乱数组
    indices = np.arange(fits.shape[0])
    random.shuffle(indices)
    fits = fits[indices]
    pops = pops[indices]
    print(indices) 

    # 首先测试非支配排序算法 
    ranks = nonDominationSort(pops, fits) 
    print('ranks:', ranks) 
    
    # 测试拥挤度排序算法 
    dis = crowdingDistanceSort(pops,fits,ranks) 
    print("dis:", dis) 


        









             
            
        


