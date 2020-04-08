import math

def promien(a=1, b=0, x=0, y=0):
    r=math.sqrt(pow(x-a, 2)+pow(y-b, 2))
    return r
a=float(input("Podaj współrzędną x środka okręgu: "))
b=float(input("Podaj współrzędną y środka okręgu: "))
x=float(input("Podaj współrzędną x punktu, przez który przechodzi okrąg: "))
y=float(input("Podaj współrzędną y punktu, przez który przechodzi okrąg: "))
print(promien(a, b, x, y))
