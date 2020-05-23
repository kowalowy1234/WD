import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
n=20
for clr, mkr, zl, zh in [('r', 'o', 10, 40), ('b', '^', 25, 50), ('g', 'h', 25, 50), ('y', 'D', 25, 50), ('b', 'x', 25, 50)]:
    x=randrange(n, zl, zh)
    y=randrange(n, zl, zh)
    z=randrange(n, zl, zh)
    ax.scatter(x, y, z, c=clr, marker=mkr)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

