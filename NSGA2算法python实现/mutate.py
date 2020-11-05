"""变异算子 
采用多项式变异 
"""
import numpy as np 

def mutate(pops, pm, etaM, lb, rb): 
    nPop = pops.shape[0] 
    for i in range(nPop):
        if np.random.rand() < pm:
            polyMutation(pops[i], etaM, lb, rb) 
    return pops 

def polyMutation(chr, etaM, lb, rb): 
    # 多项式变异 
    pos1, pos2 = np.sort(np.random.randint(0,len(chr),2)) 
    pos2 += 1 
    u = np.random.rand() 
    if u < 0.5:
        delta = (2*u) ** (1/(etaM+1)) - 1 
    else:
        delta = 1-(2*(1-u)) ** (1/(etaM+1)) 
    chr[pos1:pos2] += delta 
    chr[chr<lb] = lb 
    chr[chr>rb] = rb 

