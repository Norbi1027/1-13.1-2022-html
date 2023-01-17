
a = input("Add meg a vizsgázó nevét! ")
def atment_e(b):
    if b>=48:
        return True
    else:
        return False

while a != "":
    b = int(input("Add meg a pontszámot! "))
    if atment_e(b) == True:
        print(a,"vizsgája sikeres!")
    else:
        print(a,"vizsgája sikertelen!")
    a = input("Add meg a vizsgázó nevét! ")

