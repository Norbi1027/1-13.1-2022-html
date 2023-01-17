a = int(input("Kérem az első évszámo: "))
b = int(input("Kérem a másik évszámot: "))
t = []
for x in range(a,b):
    if x %4 == 0:
        t.append(x)
print(t[x])