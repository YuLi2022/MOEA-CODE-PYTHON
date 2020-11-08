# -*- encoding: utf-8 -*-
'''
@File    :   MOPSO.py
@Time    :   2020/11/06 
@Author  :   Yu Li 
@describe:   多目标粒子群算法主程序 
'''

from initPops import initPops
from updatePBest import updatePBest
from checkArchive import checkArchive
from getGBest import getGBest
from updateArchive import getNonDominationPops, updateArchive
from fitness import fitness
import numpy as np 

def MOPSO(nIter, nPop, nAr, nChr, func, c1, c2, lb, rb, Vmax, Vmin, M):
    """多目标粒子群算法
    Params:
        nIter: 迭代次数 
        nPOp: 粒子群规模 
        nAr: archive集合的最大规模 
        nChr: 粒子大小 
        func: 优化的函数
        c1、c2: 速度更新参数 
        lb: 解下界
        rb：解上界 
        Vmax: 速度最大值 
        Vmin：速度最小值 
        M: 划分的栅格的个数为M*M个
    Return:
        paretoPops: 帕累托解集
        paretoPops：对应的适应度 
    """
    # 种群初始化 
    pops, VPops = initPops(nPop, nChr, lb, rb, Vmax, Vmin) 
    # 获取个体极值和种群极值 
    fits = fitness(pops, func) 
    pBest = pops 
    pFits = fits 
    gBest = pops
    # 初始化archive集, 选取pops的帕累托面即可
    archive, arFits = getNonDominationPops(pops, fits) 
    wStart = 0.9 
    wEnd = 0.4  

    # 开始主循环 
    iter = 1 
    while iter <= nIter:
        print("【进度】【{0:20s}】【正在进行{1}代...】【共{2}代】".\
            format('▋'*int(iter/nIter*20), iter, nIter), end='\r') 

        # 速度更新 
        w = wStart - (wStart-wEnd) * (iter/nIter)**2 
        VPops = w*VPops + c1*np.random.rand()*(pBest-pops) + \
            c2*np.random.rand()*(gBest-pops) 
        VPops[VPops>Vmax] = Vmax 
        VPops[VPops<Vmin] = Vmin 
        # 坐标更新 
        pops += VPops 
        pops[pops<lb] = lb 
        pops[pops>rb] = rb  # 防止过界 
        fits = fitness(pops, func) 

        # 更新个体极值 
        pBest, pFits = updatePBest(pBest, pFits, pops, fits) 
        # 更新archive集 
        archive, arFits = updateArchive(pops, fits, archive, arFits) 
        # 检查是否超出规模，如果是，那么剔除掉一些个体 
        archive, arFits = checkArchive(archive, arFits, nAr, M)  
        gBest = getGBest(pops, fits, archive, arFits, M)  # 重新获取全局最优解
        iter += 1 
    print('\n')
    paretoPops, paretoFits = getNonDominationPops(archive, arFits) 
    return paretoPops, paretoFits 



