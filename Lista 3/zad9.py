import math

def il_ciag(* liczby):
    if len(liczby)==0:
        return 0.0
    else:
        iloczyn=1.0
        for i in liczby:
            iloczyn*=i
        return iloczyn
    
print(il_ciag(1, 3, 4))
