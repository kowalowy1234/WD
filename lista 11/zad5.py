import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.add_subplot(121, projection = '3d' )
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap =cm.Greys,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

X2 = np.arange(- 5 , 5 , 0.1 )
Y2 = np.arange(- 5 , 5 , 0.1 )
XX2, YY2 = np.meshgrid(X2, Y2)
R = np.sqrt(XX2** 2 + YY2** 2 )
Z = np.sin(R)
ax2 = fig.add_subplot(122, projection = '3d' )
surf2 = ax2.plot_surface(XX2, YY2, Z, cmap =cm.Blues,
linewidth = 0 , antialiased = True )
ax2.set_zlim(- 1.01 , 1.01 )
ax2.zaxis.set_major_locator(LinearLocator( 10 ))
ax2.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
plt.show()

