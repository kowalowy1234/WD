import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


df=pd.read_csv('zamowienia.csv', delimiter=";")
group=df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres=group.plot.bar()
wykres.set_ylabel('Ilość złożonych zamówień')
wykres.set_xlabel('Sprzedawca')
wykres.legend()
plt.title('Ilość zamowien złożonych przez poszczególnych sprzedawców')
plt.show()

