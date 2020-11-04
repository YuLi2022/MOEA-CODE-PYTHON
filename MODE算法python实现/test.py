# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/11/04 
@Author  :   Yu Li 
@describe:   使用fun算例测试多目标MODE 
'''
import matplotlib.pyplot as plt
from MODE import * 
from function import * 
from fitness import * 

def main(): 
    nIter = 100      
    nChr = 3 
    nPop = 50  
    F = 0.2 
    Cr = 0.9   
    func = function 
    lb = -2 
    rb = 2 
    paretoPops, paretoFits = MODE(nIter, nChr, nPop, F, Cr, func, lb, rb) 
    # print(paretoFits) 
    print(f"paretoFront: {paretoFits.shape}") 

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

    # print(paretoPops) 

if __name__ == "__main__": 
    main() 