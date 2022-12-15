class konyv:
    def __init__(self,cim,oldal,mufaj):
        self.cim = cim
        self.oldal = oldal
        self.mufaj = mufaj

print("könyvbevevő")
a=konyv(input("Cím: "),int(input("oldal: ")),input("műfaj: "))
print(a.cim)
print(a.oldal)
print(a.mufaj)
