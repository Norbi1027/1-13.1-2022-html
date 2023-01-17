lista = []
file = open("házifeladat py\\info.txt","r")
for line in file:
   lista.append(line)
file.close()

for line in lista:
    if "info" in line:
        print(line)
