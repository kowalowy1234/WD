import sys

class Material:
    def __init__(self, rodzaj, długosc, szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=długosc
        self.szerokosc=szerokosc

    def wyswietl_nazwe(self):
        return self.rodzaj+" "+self.dlugosc+" "+self.szerokosc
    

class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo

    def wyswietl_dane(self):
        return self.rozmiar+" "+self.kolor+" "+self.dla_kogo

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra

    def wyswietl_dane(self):
        return self.rodzaj_swetra

Bawełna=Material("bawełna", "1", "1")
print(Bawełna.wyswietl_nazwe())
Bluza=Ubrania("xl", "czerń", "męska")
print(Bluza.wyswietl_dane())
Sw=Sweter("zapinany")
print(Sw.wyswietl_dane())
