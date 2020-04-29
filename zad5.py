import numpy as np

def diag(n):
    a=np.diag([n for n in range(n, 0, -1)])
    return a
    
print(diag(6))
