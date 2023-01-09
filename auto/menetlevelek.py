from classes import Menetlevél
r = open("fogyasztas.txt", "r")
jarmuvek = []

for line in r:
    jarmu_adatok = line.split(";")
    jarmu = Menetlevél(jarmu_adatok[0])
    jarmu.setMegtettkm(int(jarmu_adatok[1]))
    jarmu.setÖsszÜzemanyag(float(jarmu_adatok[2][0:len(jarmu_adatok[2])]-2))
    jarmuvek.append(jarmu)
r.close()

r = open("atlagfogyasztas.txt","w")
for jarmu in jarmuvek:
    r.write(f"{jarmu.getrendszam()},{jarmu.atlagfogyasztas()} \n")
    print(f"{jarmu.getrendszam()},{jarmu.atlagfogyasztas()}")
r.close()