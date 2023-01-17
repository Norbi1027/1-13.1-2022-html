
class teszt:
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
        return irany

    def nap_nev(nap):
        napok = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]
        if nap <= 0 and nap >= 0:
            print(napok[nap])
        else:
            print("none")

    def nap_szam(nap):
        napok = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]
        print(napok[str(nap] )
  
teszt.irany("é")
teszt.nap_nev(7)
teszt.nap_szam("hétfő")

