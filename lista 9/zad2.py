import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xls=pd.ExcelFile('Imiona.xlsx')
df=pd.read_excel(xls, 'Arkusz1')
group=df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres=group.plot.bar()
wykres.set_ylabel('Liczba urodzonych dzieci (wyrażona w milionach)')
wykres.set_xlabel('Płeć')
wykres.legend()
plt.title('Liczba urodzonych chłopców i dziewczynek z danego okresu')
plt.show()

