import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xls=pd.ExcelFile('Imiona.xlsx')
df=pd.read_excel(xls, 'Arkusz1')
group=df.groupby(['Rok']).agg({'Liczba':['sum']})
group.plot()
plt.show()

