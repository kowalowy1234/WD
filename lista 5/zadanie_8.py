class Sam:

    def __init__(self, wyraz):
        self.wyraz=wyraz
        self.samogloski="aeyuioóąę"
        self.index=0
        self.pom_index=0

    def zwroc_wyraz(self):
        return self.wyraz

    def __next__(self):
        if isinstance(self.wyraz, str):
            if self.index==len(self.wyraz):
                raise StopIteration
            else:
                for i in range(0, len(self.samogloski)-1):
                    self.pom_index=self.index
                    if self.wyraz[self.index]==self.samogloski[i]:
                        self.index+=1
                        return self.wyraz[self.pom_index]
        else:
            return "To nie jest string!"

wyraz=Sam("Pięćdziesięciogroszówka")
for i in range(0, len(wyraz.zwroc_wyraz())-1):
    print(wyraz.__next__())
