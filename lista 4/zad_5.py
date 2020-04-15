class Ciag:

    def __init__(self, ciag):
        self.ciag=ciag

    def pobierz_elementy(self):
        n=input(print("podaj ilość elementów: "))
        self.ciag=[]
        for i in range(0, n):
            self.ciag.append(input());

    def pobierz_parametry(self):
        self.ciag=[]
        a1=int(input("podaj pierwszy wyraz ciągu: "))
        r=int(input("podaj różnicę wyrazów ciągu: "))
        n=int(input("podaj ilość elementów ciągu: "))
        self.ciag.append(a1)
        for i in range(1, n):
            self.ciag.append((a1+(i*r)));
            
    def policz_sume(self):
        suma=0
        length=len(self.ciag)
        for i in range(length):
            suma+=self.ciag[i];
        return suma

T=[]
ciag=Ciag(T)
ciag.pobierz_parametry()
print(ciag.policz_sume())
    
