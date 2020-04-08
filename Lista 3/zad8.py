import math

def s_ciag(a1=1, r=1, ile=10):
    an=a1+(ile-1)*r
    suma=((a1+an)/2)*ile
    return suma
a1=float(input("Podaj pierwszy wyraz dowolnego ciągu arytmetycznego: "))
r=float(input("Podaj różnicę wyrazów dowolnego ciągu arytmetycznego: "))
ile=float(input("Podaj ilość wyrazów do zsumowania: "))
print(s_ciag(a1, r, ile))
