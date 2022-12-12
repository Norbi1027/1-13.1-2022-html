def paros_ossz():
    t = [1,2,3,4,5,6,7,8,9,10,11,25,48,41,51,32]
    osszeg = 0
    for i in t:
        if i%2==0:
            osszeg = i+osszeg
    return osszeg

print(paros_ossz())