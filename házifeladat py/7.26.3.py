def negativ_osszeg():
    t = [-10,-20,-30,5,8,-40]
    l = []
    for i in t:
        if i<0:
            l.append(i)
    return l

print(negativ_osszeg())