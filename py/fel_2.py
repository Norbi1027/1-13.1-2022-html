def hoe(a):
    b=False
    if a>150:
        b=True
    return b

cim = input("cím:")
while(cim!=""):
    oldal = int(input("oldalak:"))
    old=hoe(oldal)
    if old:
        print("A könyv hosszú")
    else:
        print("A könyv rövid")
    cim=input("cím:")