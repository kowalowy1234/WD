import numpy as np

def add(a, b):
    return a+b

sinus=np.array([7, 8, 9, 10, 11, 12]).reshape(2, 3)
a=np.sin(sinus)
cosinus=np.array([7, 8, 9, 10, 11, 12]).reshape(2, 3)
b=np.cos(cosinus)
print(add(a, b))
