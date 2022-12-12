def paros():
    t = [1,2,3,4,5,6,7,8,9,10,11,25,48,41,51,32]
    paros = 0
    for i in t:
        if i%2==0:
            paros=paros+1
    return paros

print(paros())