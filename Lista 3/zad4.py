def monotonicznosc(a):
    if(a>0):
        return "funkcja jest rosnąca"
    elif(a<0):
        return "funkcja jest malejąca"
    else:
        return "funkcja jest stała"
a=float(input("Podaj współczynnik a wyrażenia: "))
print(monotonicznosc(a))
