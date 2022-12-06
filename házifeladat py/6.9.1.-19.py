
class teszt:
    #1.feladat
    def irany(irany):
        if irany == "é" and "É":
            print("Kelet")
        elif irany == "k" and "K":
            print("Dél")
        elif irany == "d" and "D":
            print("NYugat")
        elif irany == "ny" and "NY":
            print("Észak")
        else:
            print("none")
    #2.feladat
    def nap_nev(nap):
        napok = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]
        if nap >=0:
            print(napok[nap])
        else:
            print("none")

    #3.feladat
    def nap_szam():
        napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

        napIn = input("Ajd meg egy napot! ").lower()
        napIndex = None

        for i in range(0, len(napok)):
            if napIn == napok[i].lower():
                napIndex = i

        print(napIndex)

    #4.feladat
    def nap_nyaralas():
        napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

        mikor =int(input("Hány nap mulva mész nyaralni? "))

        napIn = input("Milyen nap van ma? ").lower()
        napIndex = None

        for i in range(0, len(napok)):
            if napIn == napok[i].lower():
                napIndex = i
        vissza = (napIndex + mikor)%7 

        print("Ma",napIn,"van",mikor,"nap mulvan mész nyaralni, az a nap:",napok[vissza])

    #5.feladat
    def nap_nyaralasminusz():

        napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

        mikor =int(input("Hány nap mulva mész nyaralni? "))

        napIn = input("Milyen nap van ma? ").lower()
        napIndex = None

        for i in range(0, len(napok)):
            if napIn == napok[i].lower():
                napIndex = i
        vissza = (napIndex + mikor)%7 

        print("Ma",napIn,"van",mikor,"nappal ezelőtt voltál nyaralni, az a nap:",napok[vissza])

    #6.feladat
    def honap_nap():
        honap = ["Január","Február","Március","Április","Május","június","Július","Agusztus","Szeptember","Október","November","December"]
        nap =[31,28,31,30,31,30,31,31,30,31,30,31]

        honapIn = input("Adja meg a hónapot! ").lower()
        honapIndex = None

        for i in range(0, len(honap)):
            if honapIn == honap[i].lower():
                honapIndex = i

        print("Ma",honapIn,"van","ami:",nap[honapIndex],"napos.")

    #7.feladat
    def masodperc_valtas():
        ora = int(input("ora: "))
        perc = int(input("Perc: "))
        masodperc = int(input("masodperc: "))
        orav = ora * 3600
        percv = perc * 60
        osszeg = orav + percv + masodperc
        print(int(osszeg))

    #8.feladat
    def masodperc_valtas2():
        ora = float(input("ora: "))
        perc = float(input("Perc: "))
        masodperc = float(input("masodperc: "))
        orav = ora * 3600
        percv = perc * 60
        osszeg = orav + percv + masodperc
        print(int(osszeg))

    #9.feladat
    def valtas():
        masodperc = int(input("másodperc: "))
        ora = masodperc/3600
        orav = masodperc%3600 
        perc = orav/60
        perv = orav%60
        masodpercv = perv
        print(int(ora)," óra",int(perc),"perc",masodpercv,"másodperc")

    #11.feladat
    def osszehasonlito():
        a = int(input("Első szám: "))
        b = int(input("masodik szám: "))

        if a>b:
            print("1")
        elif a<b:
            print("-1")
        else:
            print("0")
    #12.feladat
    def atfogo():
        bef1 = int(input("1. befogó: "))
        bef2 = int(input("2. befogó: "))
        atfogo = ((bef1*bef1)+(bef2*bef2)) ** 0.5
        print(atfogo)

    #13.feladat
    def meredekseg(x1,y1,x2,y2):
        return (y1-y2)/(x1-x2)

        print(meredekseg(5,3,4,2))
        print(meredekseg(1,2,3,2))
        print(meredekseg(1,2,3,3))
        print(meredekseg(2,4,1,2))
        print(meredekseg(1,6,3,12))
    
    #14.feladat
    def paros_e(n):
        if n%2 == 0: return True
        else: return False
    #15.feladat
    def paratlan_e(n):
        if n%2 !=0:
            return True
        else:
            return False

    #16.feladat
    def tenyezo_e(t, n):
        if n%t==0: return True
        else: return False

    #17.feladat
    def tobbszorose_e(t, n):
        if t%n==0:
            return True
        else:
            return False

    #18.feladat
    def celsiusra_valtas(f):
        return int(((f-32)/9)*5)

    #19.feladat
    def Fahrenheit_valtas(c):
        return int(((c/5)*9)+32)


teszt.irany("é")
teszt.nap_nev(3)
teszt.nap_szam()
teszt.nap_nyaralas()
teszt.nap_nyaralasminusz()
teszt.honap_nap()
teszt.masodperc_valtas()
teszt.masodperc_valtas2()
teszt.valtas()
teszt.osszehasonlito()
teszt.atfogo()
teszt.meredekseg(5,3,4,2)
print(teszt.paros_e(4))
print(teszt.paratlan_e(3))
print(teszt.tenyezo_e(3, 12))
print(teszt.tobbszorose_e(12,3))
print(teszt.celsiusra_valtas(212))
print(teszt.Fahrenheit_valtas(0))
