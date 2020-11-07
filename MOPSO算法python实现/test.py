# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/11/07 
@Author  :   Yu Li 
@describe:   测试MOPSO主程序 
'''

from MOPSO import MOPSO
import numpy as np 
import matplotlib.pyplot as plt 
from function import function
from fitness import * 

def test():

    nIter = 100   
    nPop = 100           
    nAr = 100      
    nChr = 3 
    func = function 
    c1 = 1.49445
    c2 = 1.49445
    lb = -2 
    rb = 2 
    Vmax = 0.2 
    Vmin = -0.2 
    paretoPops, paretoFits = MOPSO(nIter, nPop, nAr, nChr, \
        func, c1, c2, lb, rb, Vmax, Vmin) 
    
    print(paretoPops.shape) 
    print('='*20) 
    #print(paretoPops) 

     # 理论最优解集合 
    x = np.linspace(-1/np.sqrt(3), 1/np.sqrt(3), 116).reshape(116,1) 
    X = np.tile(x, 3)  # 理论最佳帕累托解集 
    thFits = fitness(X, function) 

    plt.rcParams['font.sans-serif'] = 'KaiTi'  # 设置显示中文 
    fig = plt.figure(dpi=400) 
    ax = fig.add_subplot(111) 
    ax.plot(thFits[:,0], thFits[:,1], color='green',\
         label="理论帕累托前沿") 
    ax.scatter(paretoFits[:,0], paretoFits[:,1], \
        color='red', label="实际求解") 
    ax.legend() 
    fig.savefig('test.png', dpi=400) 


if __name__ == "__main__":
    test() 
    
