import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xls=pd.ExcelFile('Imiona.xlsx')
df=pd.read_excel(xls, 'Arkusz1')
last=df[df['Rok']>2012]
print(last)
group=last.groupby(['Plec']).agg({'Liczba':['sum']})
wykres=group.plot.pie(subplots=True, autopct='%.2f %%', fontsize=15, figsize=(6, 6))
plt.title('% ilość urodzonych dzieci w danym okresie z podziałem na płeć')
print(group)
plt.show()

