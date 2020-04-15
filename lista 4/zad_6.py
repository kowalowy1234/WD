class Slowa:

    def __init__(self, a, b):
        self.a=a
        self.b=b

    def czy_palindrom(self):
        a_r=''.join(reversed(self.a))
        if(a_r==a):
            return True

    def czy_metagramy(self):
        if(len(self.a)!=len(self.b)):
            return False
        else:
            length=len(self.a)
            diff=0
            for i in range(length):
                if(self.a[i]!=self.b[i]):
                    diff+=1
            if(diff==1):
                return True
            else:
                return False

    def czy_anagramy(self):
        a_s=''.join(sorted(self.a))
        b_s=''.join(sorted(self.b))
        if(a_s==b_s):
            return True
        else:
            return False

    def wyswietl_wyrazy(self):
        return a+", "+b

a="kajak"
b="kijak"
wyrazy=Slowa(a, b)
print(wyrazy.wyswietl_wyrazy())
print(wyrazy.czy_palindrom())
print(wyrazy.czy_metagramy())
print(wyrazy.czy_anagramy())

    
