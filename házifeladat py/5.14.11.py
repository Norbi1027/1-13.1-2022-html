a = int(input("első oldal:"))
b = int(input("második oldal:"))
c = int(input("harmadik oldal:"))

def haromszog():
    if (a**2+b**2) == c**2:
        print("derékszögü")
    else:
        print("nem derékszögű")

haromszog()

