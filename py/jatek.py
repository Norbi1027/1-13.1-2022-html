import random

név = input("Írd be a játékos nevedet: ")
print("")
print("Üdvözölleg",név,"az első játékomba!")
print("")
szint = int(input("Válassz egy nehézségi szintet! (1-3)"))
print("")
karakter_valasztas = input("Válassz egy role-t! (tank,assasin,mage)")
hp = 0
erő = 0
kitérés = 0
szerencse = random.randint(0,100)
pénz = 0
enemy_hp = random.randint(40,100)
enemy_erő = random.randint(1,10)
enemy_kitérés = random.randint(1,10)
vége = False

while (karakter_valasztas != "oké"):
    if karakter_valasztas == "tank":
            hp = 150
            erő = 7
            kitérés = 92
            print("hp: 150   erő:7    kitérés:3")
            
    elif karakter_valasztas =="assasin":
            hp = 50
            erő = 12
            kitérés = 101
            print("hp: 50   erő:12    kitérés:8")
            
    elif karakter_valasztas =="mage":
            hp = 100
            erő = 10
            kitérés = 93
            print("hp: 100   erő:10    kitérés:5")
    karakter_valasztas = input("Válassz egy role-t! (tank,assasin,mage)")



def szerencse():
    while hp != 1000:
        szerencse = random.randint(0,100)
        if szerencse > 70:
            return True
        else:
            return False

def szerencsee():
    while hp != 1000:
        szerencs = random.randint(0,100)
        if szerencs > kitérés:
            return False
        else:
            True


while (vége !=True):
    print("----------------------------------------------")
    print("")
    print("Az enemy stata: ","erő: ",enemy_erő,"hp: ",enemy_hp,"kitérés: ",enemy_kitérés)
    print("")
    print("----------------------------------------------")
    lépés = input("Válassz egy lépést! (támadás,kritikál)")
    print("")
    if lépés == "támadás":
        enemy_hp = enemy_hp-erő 
    elif lépés == "kritikál" and szerencsee() == True :
        enemy_hp = enemy_hp-(erő*2)
        print("sikerült kritikus találatot bevinni")
        print("")
    elif lépés == "kritikál" and szerencsee() == False :
        print("nem sikerült kritikus találatot bevinni")
        print("")
    print("Az enemy új stata: ","erő: ",enemy_erő," hp: ",enemy_hp," kitérés: ",enemy_kitérés)
    print("")
    print("----------------------------------------------")
    print("Most az enemy következik")
    print("")

    if szerencse() == True:
        print("Az ellenfél nem tudod bevinni egy ütést")
        print("")
    else:
        hp = hp-enemy_erő

    print("Az új hp:",hp)

    if enemy_hp <=0:
        print("Legyőzted")
    
    if hp <= 0:
        print("Meghaltál!")

    print("")
    if hp <= 0 or enemy_hp <= 0:
        vége = True
    else:
        False
    print("----------------------------------------------")
