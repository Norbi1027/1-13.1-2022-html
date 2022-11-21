import random
# = [1,3,5,7,"jolán"]
#print(t)

t=[]
for x in range(5):
    t.append(random.randint(0,20))
print(t)
#összegzés tétel
osszeg=0
for x in t:
    osszeg+=x
print(osszeg)
#átlag tétel
alt=osszeg/len(t)
print(alt)
#minimum
min=21
for x in t:
    if min>x:
        min=x
print(min)
#maximum
max=-1
for x in t:
    if max<x:
        max=x
print(max)
#keresés
