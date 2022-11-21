a = int((input("A:")))
b = int((input("B:")))

if a<0 and b<0:
    print("Mindkét szám negatív")
elif a>=0 and b>=0:
    print("Mindkét szám pozitív")
elif a<0:
    print("Az első szám negatív")
elif b<0:
    print("Az második szám negatív")