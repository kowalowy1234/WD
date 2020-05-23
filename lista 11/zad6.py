import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.add_subplot(121, projection = '3d' )
z=np.arange(5)
x=np.sin(z)
y=np.sin(2*z)
ax.plot(x, y, z, label="wykres liniowy")

bx=fig.add_subplot(122, projection='3d')
z2=np.arange(20)
y2=np.sin(z2)
x2=np.sin(2*z2)
bx.scatter(x2, y2, z2, label="wykres punktowy")
plt.show()

