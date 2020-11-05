"""交叉算子 
采用模拟二进制交叉SBX(Simulated Binary Crossover) 
"""
import numpy as np 

def crossover(pops, pc, etaC, lb, rb):
    # 拷贝父代种群，以防止改变父代种群结构  
    chrPops = pops.copy()  
    nPop = chrPops.shape[0]
    for i in range(0, nPop, 2): 
        if np.random.rand() < pc: 
            SBX(chrPops[i], chrPops[i+1], etaC, lb, rb)  # 交叉 
    return chrPops 


def SBX(chr1, chr2, etaC, lb, rb):
    # 模拟二进制交叉
    pos1, pos2 = np.sort(np.random.randint(0,len(chr1),2)) 
    pos2 += 1 
    u = np.random.rand()
    if u <= 0.5:
        gamma = (2*u) ** (1/(etaC+1))
    else:
        gamma = (1/(2*(1-u))) ** (1/(etaC+1)) 
    x1 = chr1[pos1:pos2] 
    x2 = chr2[pos1:pos2] 
    chr1[pos1:pos2], chr2[pos1:pos2] = 0.5*((1+gamma)*x1+(1-gamma)*x2), \
        0.5*((1-gamma)*x1+(1+gamma)*x2) 
    # 检查是否符合约束 
    chr1[chr1<lb] = lb 
    chr1[chr1>rb] = rb 
    chr2[chr2<lb] = lb 
    chr2[chr2<rb] = rb


    




