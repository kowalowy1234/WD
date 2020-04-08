def if_par(a1, a2):
    if(a1==a2): return "Proste są równoległe"
    elif(a1*a2==-1): return "Proste są prostopadłe"
    else: return "Proste nie są ani równoległe ani prostopadłe"
a1=float(input("Podaj współczynnik a pierwszej prostej: "))
a2=float(input("Podaj współczynnik a drugiej prostej: "))
print(if_par(a1, a2))
