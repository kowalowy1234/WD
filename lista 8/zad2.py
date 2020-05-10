import numpy as np
import pandas as pd
import xlrd
import openpyxl


xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx, 'Arkusz1')

#print(df[df['Liczba']>1000])

#print(df[df['Imie']=='PIOTR'])

#print(df['Liczba'].sum())

#print(df.loc[df['Rok']<2006, 'Liczba'].sum())

#print(df.groupby(df['Plec']).agg({'Liczba':['sum']}))

#print(df.sort_values('Liczba', ascending=False).groupby(['Rok','Plec']).nth(0))

#print(df.sort_values('Liczba', ascending=False).groupby(['Plec']).nth(0))

