import random
f = open("szavak\\ige.txt","r",encoding="utf-8")
a1 = f.readline()
f.close()

f = open("szavak\\melleknev.txt","r",encoding="utf-8")
a2 = f.readline()
f.close()

f = open("szavak\\mgh.txt","r",encoding="utf-8")
a3 = f.readline()
f.close()
ige = a1.split(" ")
mel=a2.split(" ")
mgh=a3.split(" ")
nev = input("Ki?")
hol = input("Hol?")
ig = ige[random.randint(0,len(ige)-1)]
m1 = mel[random.randint(0,len(mel)-1)]
m2 = mel[random.randint(0,len(mel)-1)]
print(m1,nev,ig,m2,hol)