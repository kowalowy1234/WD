import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


df=pd.read_csv('iris.csv', delimiter=",")
y=df['sepal_width']
x=df['petal_width']
plt.scatter(x, y, label='wykres rozproszony', color='g')
plt.show()

