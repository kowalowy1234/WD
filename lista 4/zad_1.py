import sys

liczby = [i for i in range(0, 51) if i%4==0]
plik=open('podzielne.txt', 'a+')
plik.writelines(str(liczby))
plik.close()
