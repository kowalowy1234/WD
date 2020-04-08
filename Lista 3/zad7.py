import math

def promien(a=1, b=1):
    c=math.sqrt(pow(a, 2)+pow(b, 2))
    return c
a=float(input("Podaj pierwszą przyprostokątną: "))
b=float(input("Podaj drugą przyprostokątną: "))
print(promien(a, b))
