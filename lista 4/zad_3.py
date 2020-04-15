import sys

with open('tekst.txt', 'a+') as plik:
    for i in range(0, 5):
        plik.writelines("Linia numer "+str(i)+"\n")
with open('tekst.txt', 'r') as plik:
    for linia in plik:
        print(linia, end="")
