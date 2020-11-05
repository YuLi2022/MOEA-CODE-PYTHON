"""
测试NSGA2算法 
"""
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis 
from NSGA2 import * 
from function import * 
from fitness import * 

def main(): 
    nIter = 10   
    nChr = 3 
    nPop = 100 
    pc = 0.6  
    pm = 0.1 
    etaC = 1 
    etaM = 1 
    func = function 
    lb = -2 
    rb = 2 
    paretoPops, paretoFits = NSGA2(nIter, nChr, nPop, pc, pm, etaC, etaM, func, lb, rb) 
    print(paretoFits) 
    print(f"paretoFront: {paretoFits.shape}") 

    # 理论最优解集合 
    x = np.linspace(-1/np.sqrt(3), 1/np.sqrt(3), 116).reshape(116,1) 
    X = np.concatenate((x,x,x), axis=1) 
    thFits = fitness(X, function) 

    fig = plt.figure(dpi=400) 
    ax = fig.add_subplot(111) 
    ax.plot(thFits[:,0], thFits[:,1], color='green') 
    ax.scatter(paretoFits[:,0], paretoFits[:,1], color='red') 
    fig.savefig('test.png', dpi=400) 

    print(paretoPops) 

if __name__ == "__main__": 
    main() 