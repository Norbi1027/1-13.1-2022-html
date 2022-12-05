
class teszt:
    #1.feladat
    def irany():
        irany = input("Válassz egy égtájat! (é,k,d,ny)") 
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
        return irany
    #2.feladat
    def nap_nev():
        nap = int(input("Adj meg egy napnak a számát(0-6-ig)"))
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

# teszt.irany()
# teszt.nap_nev()
# teszt.nap_szam()
# teszt.nap_nyaralas()
# teszt.nap_nyaralasminusz()
# teszt.honap_nap()
# teszt.masodperc_valtas()
# teszt.masodperc_valtas2()
teszt.valtas()