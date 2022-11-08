import random

szam_1=random.randint(1,100)
szam_2=random.randint(1,100)
szam_3=random.randint(1,100)

print("Első szám:",szam_1)
print("Második szám:",szam_2)
print("Harmadik szám:",szam_3)

if szam_1<szam_2 and szam_1<szam_3:
    print(szam_1)

if szam_2<szam_1 and szam_2<szam_3:
    print(szam_2)

if szam_3<szam_1 and szam_3<szam_2:
    print(szam_3)