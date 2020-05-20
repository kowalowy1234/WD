import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
import random as rd

def rzucaj(x):
    rzuty=[rd.randint(1, 6) for i in range(1,x+1)]
    return rzuty
n=7
wynik=rzucaj(n)
print(wynik)
plt.hist(wynik, bins=n, facecolor='red', density=False, label='rzut')
plt.xlabel('ilość oczek w rzucie')
plt.ylabel('ilość trafień')
plt.legend()
plt.show()

