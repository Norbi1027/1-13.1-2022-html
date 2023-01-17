class hiresseg:
    def __init__(self,nev,foglalkozas,nemzetiseg):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg = nemzetiseg

    def nemzetisegg(nemzetiseg):
        if nemzetiseg == "a":
            return "Ms."
        elif nemzetiseg == "n":
            return "Frau"
    
t=[]
for x in range(3):
    nev = input("Add meg egy híres női nevet! ")
    foglalkozas = input("Add meg a foglalkozását! ")
    nemzetiseg = input("Add meg a nemzetiségét (a/n)")
    t.append(hiresseg(nev,foglalkozas,nemzetiseg))
for x in range(3):
    print(hiresseg.nemzetisegg(t[x].nemzetiseg),t[x].nev,"egy híres",t[x].foglalkozas)