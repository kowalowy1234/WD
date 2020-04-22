class Parzyste:

    def __init__(self, wyraz):
        self.wyraz=wyraz
        self.index=0
        self.p_index=0

    def zwroc_wyraz(self):
        return self.wyraz

    def generator(self):
        for i in range(0, len(self.wyraz)-1, 1):
            if i==0:
                yield self.wyraz[i]
            elif i%2==0:
                yield self.wyraz[i]
            else:
                yield "nieparzysty indeks"  

        
        
            

wyraz=Parzyste("Pięćdziesięciogroszówka")
print(next(wyraz.generator()))

        
