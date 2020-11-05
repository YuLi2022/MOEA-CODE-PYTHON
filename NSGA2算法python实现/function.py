"""
优化的目标函数，返回多个目标函数值 
"""
import numpy as np 

def function(X):
    y1 = 1 - np.exp(-np.sum((X-1/np.sqrt(3))**2)) 
    y2 = 1 - np.exp(-np.sum((X+1/np.sqrt(3))**2)) 
    return y1, y2 

if __name__ == "__main__":
    tX = np.array([-0.57735, -0.57735, -0.57735]) 
    print(function(tX))