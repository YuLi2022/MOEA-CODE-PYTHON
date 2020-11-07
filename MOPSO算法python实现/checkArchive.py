from collections import Counter
import random 
from getGBest import getPosition
import numpy as np 

def checkArchive(archive, arFits, nAr, M):
    """
    检查archive集是否超出了规模。
    如果超出了规模那么采取减少操作 
    """
    if archive.shape[0] <= nAr:
        return archive, arFits 
    else:
        nA = archive.shape[0]  # 当前解集大小 
        flags = getPosition(archive, arFits, M) 
        # 统计每个网格出现的次数
        counts = Counter(flags).most_common() 
        # 选择原始archive集
        isCh = np.array([True for i in range(nA)]) 
        indices = np.arange(nA)  # 原始索引  
        for i in range(len(counts)):
            if counts[i][-1] > 1: 
                # 删除当前网格counts[i][0]的粒子数 
                pn = int((nA-nAr)/nA*counts[i][-1]+0.5) 
                # if counts[i][-1] >= 10:
                #     pn = counts[i][-1] // 2
                # 当前要删除的网格中的所有粒子的索引 
                gridIdx = indices[flags==counts[i][0]].tolist() 
                pIdx = random.sample(gridIdx, pn) 
                isCh[pIdx] = False  # 删除这些元素 
        archive = archive[isCh] 
        arFits = arFits[isCh] 
        return archive, arFits 




        
