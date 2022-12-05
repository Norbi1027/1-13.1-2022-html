#1.feladat
# a = int(input("Első szám:"))
# b = int(input("Második szám:"))

# if a>b:
#     print("Az A nagyobb")
# elif a<b:
#     print("A B nagyobb")
# else:
#     print("egyenlő a két szám")

#2.feladat

# def magase(mag):
#     if mag>170:
#         return True
#     else:
#         return False

# nev = input("Név: ")
# while(nev!=""):
#     m = int(input("Magasság: "))
#     if magase(m):
#         print(nev,"Magasabb mint az átlag!")
#     else:
#         print(nev,"Nem magasabb mint az átlag!")
#     nev= input("név: ")

#3.feladat

import random

class szere:
    def __init__(self,nev,fog,nem,szam):
        self.nev = nev
        self.fog = fog
        self.nem = nem
        self.szam = szam

    def FvN(nem):
        if nem=="f":
            return "férfi"
        elif nem=="n":
            return "nő"

t = []
for x in range(3):
    a = input("add meg a nevet! ")
    b = input("add meg a foglalkozást! ")
    c = input("add meg a nemet! (f/n) ")
    d = random.randint(1,50)
    t.append(szere(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")




