def szo():
    t = ["asdfg","dfsd","rfghb","sdfgh"]
    szam = 0
    for i in t:
        x = len(i)
        if x == 5:
            szam += 1

    return szam

print(szo())