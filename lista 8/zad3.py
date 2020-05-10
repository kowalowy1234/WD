import numpy as np
import pandas as pd
import xlrd
import openpyxl


df = pd.read_csv('zamowienia.csv', sep=';')

#print(df['Sprzedawca'].unique())

#df2=df.nlargest(5, ['Utarg'])
#print(df2['Utarg'])

#print(df.groupby(df['Sprzedawca']).agg({'idZamowienia':['count']}))

#print(df.groupby(df['Kraj']).agg({'idZamowienia':['count']}))

#print(df.loc[((df['Kraj']=='Polska') & (df['Data zamowienia']<'2006-01-01')) & (df['Data zamowienia']>'2004-12-31'), 'idZamowien'].sum())

