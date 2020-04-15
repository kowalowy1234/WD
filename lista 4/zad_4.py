class NaZakupy:
    
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
        
    def wyswietl_produkt(self):
        return self.nazwa_produktu+"; "+str(self.ilosc)+"; "+self.jednostka_miary+" ; "+str(self.cena_jed)+" zł"

    def ile_produktu(self):
        return str(self.ilosc)+" "+self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed

produkt1=NaZakupy("ziemniaki", 4, "kg", 2)
print(produkt1.wyswietl_produkt())
print(produkt1.ile_produktu())
print(produkt1.ile_kosztuje())
