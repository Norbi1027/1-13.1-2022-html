import random

szam_1 = random.randint(1,100)
print("A szám:",szam_1)

if szam_1 % 3 ==0:
    print("osztható 3-al")
if szam_1 % 5 ==0:
    print("osztahtó 5-el")
if szam_1 % 3 != 0 and szam_1 % 5 != 0:
    print("Nem osztható 3-al és 5-el se")