import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt
import random

df=pd.read_csv('iris.csv', delimiter=",")
dif=df['sepal_width']-df['sepal_length']
data={
     'y':df['sepal_width'],
     'x':df['sepal_length'],
     'c':np.random.randint(0, 50, 150),
     'd':np.abs(dif)*10 #skala zwiększona 10 razy dla przejrzystości
   }
plt.scatter('x', 'y', label='wykres punktowy', c='c', s='d', data=data)
print(data['d'])
plt.show()
