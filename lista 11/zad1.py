import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.gca(projection='3d')
z=np.arange(0, 2*np.pi)
x=np.sin(z)
y=2*np.cos(z)
ax.plot(x, y, z, label="zadanie1")
ax.legend()
plt.show()
