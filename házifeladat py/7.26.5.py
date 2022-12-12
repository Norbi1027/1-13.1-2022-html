def paros_ossz():
    t = [1,3,5,2,5,7,9]
    o = []
    for x in t:
        if x %2 != 0:
            o.append(x)
        else:
            return o
print(paros_ossz())
#ha nincs páros szám akkor none van a kimeneten
