# -*- encoding: utf-8 -*-
'''
@File    :   MODE.py
@Time    :   2020/11/04 
@Author  :   Yu Li 
@describe:   基于快速非支配排序算法的多目标差分进化算法主程序 
'''
from mutate import * 
from crossover import * 
from select1 import * 
from nonDominationSort import crowdingDistanceSort, nonDominationSort
from fitness import fitness
from initPop import initPop
import numpy as np 

def MODE(nIter, nChr, nPop, F, Cr, func, lb, rb):
    """多目标差分进化算法主程序 
    Params:
        nIter: 迭代次数
        nPop: 种群规模 
        F: 缩放因子 
        Cr: 交叉概率 
        func：优化函数 
        lb: 自变量下界 
        rb：自变量上界 
    Return：
        paretoPops: 帕累托解集 
        paretoFits: 对应的适应度 
    """
    # 生成初始种群 
    parPops = initPop(nChr, nPop, lb, rb) 
    parFits = fitness(parPops, func) 

    # 开始迭代  
    iter = 1 
    while iter <= nIter:
        # 进度条 
        print("【进度】【{0:20s}】【正在进行{1}代...】【共{2}代】".\
            format('▋'*int(iter/nIter*20), iter, nIter), end='\r')

        mutantPops = mutate(parPops, F, lb, rb)  # 产生变异向量 
        trialPops = crossover(parPops, mutantPops, Cr)  # 产生实验向量 
        trialFits = fitness(trialPops, func)  # 重新计算适应度 

        pops = np.concatenate((parPops, trialPops), axis=0)  # 合并成新的种群
        fits = np.concatenate((parFits, trialFits), axis=0) 
        ranks = nonDominationSort(pops, fits)  # 非支配排序 
        distances = crowdingDistanceSort(pops, fits, ranks)  # 计算拥挤度 

        parPops, parFits = select1(nPop, pops, fits, ranks, distances)   

        iter += 1 
    print("\n") 
    # 获取等级为0，即实际求解得到的帕累托前沿 
    paretoPops = pops[ranks==0] 
    paretoFits = fits[ranks==0] 
    
    return paretoPops, paretoFits


        

