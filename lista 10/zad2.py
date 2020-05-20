import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

x=np.arange(1,21)
print(x)
plt.plot(x, 1/x, ":^g", label='wymierna')
plt.xlabel("wartości x")
plt.ylabel("wartości f(x)=1/x")
plt.legend()
l=len(x)
plt.axis([1, l, 0, 1])
plt.show()
