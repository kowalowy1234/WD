import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

x=np.arange(0, 31, 0.1)
s=np.sin(x)
plt.plot(x, s+2, "b-", label='sin(x)')
plt.plot(x, -s, "g-", label='-sin(x)')
plt.xlabel("wartości x")
plt.ylabel("wartości sin(x)")
plt.axis([-1, 30, -1.25, 3.25])
plt.legend(loc=6)
plt.show()
