"""
种群或个体的适应度 
"""
import numpy as np 
from function import * 

def fitness(pops,func):
    # 计算种群或者个体的适应度 
    # 如果是1维需要转为2维 
    if pops.ndim == 1:
        pops = pops.reshape(1,len(pops))
    nPop = pops.shape[0] 
    fits = np.array([func(pops[i]) for i in range(nPop)]) 
    return fits 

if __name__ == "__main__":
    pops = np.array([-0.57735, -0.57735, -0.57735])  
    fits = fitness(pops, function) 
    print(fits) 