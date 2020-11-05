"""
NSGA2算法主程序 
"""
import numpy as np 
from initPops import * 
from optSelect import optSelect
from nonDominationSort import * 
from select1 import * 
from fitness import * 
from crossover import * 
from mutate import * 


def NSGA2(nIter, nChr, nPop, pc, pm, etaC, etaM, func, lb, rb): 
    """非支配遗传算法主程序 
    Params:
        nIter: 迭代次数 
        nPop: 种群大小 
        pc: 交叉概率 
        pm: 变异概率 
        func: 优化的函数 
        lb: 自变量下界
        rb: 自变量上界 
    """   
    # 生成初始种群 
    pops = initPops(nPop, nChr, lb, rb)  
    fits = fitness(pops, func) 

    # 开始第1次迭代 
    iter = 1 
    while iter <= nIter:
        print(f"当前正在第{iter}代....")
        ranks = nonDominationSort(pops, fits)  # 非支配排序 
        distances = crowdingDistanceSort(pops, fits, ranks)  # 拥挤度
        pops, fits = select1(nPop, pops, fits, ranks, distances) 
        chrpops = crossover(pops, pc, etaC, lb, rb)  # 交叉产生子种群 
        chrpops = mutate(chrpops, pm, etaM, lb, rb)  # 变异产生子种群 
        chrfits = fitness(chrpops, func)  
        # 从原始种群和子种群中筛选 
        pops, fits = optSelect(pops, fits, chrpops, chrfits)  
        iter += 1 
    # 对最后一代进行非支配排序 
    ranks = nonDominationSort(pops, fits)  # 非支配排序 
    distances = crowdingDistanceSort(pops, fits, ranks)  # 拥挤度 
    paretoPops = pops[ranks==0] 
    paretoFits = fits[ranks==0] 
    return paretoPops, paretoFits 
    




