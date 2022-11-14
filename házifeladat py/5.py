xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for x in xs:
    print (x)

for x in xs:
    print(f"A szám: {x}, a négyzete: {x*x}")

összeg=0
for x in xs:
    összeg = összeg + x

print (összeg)

Összeg = 1
for x in xs:
    Összeg = összeg * x

print(összeg)