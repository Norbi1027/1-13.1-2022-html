def szo_tisztitas(szo):
    spec = "\'\"+!%/=()~ˇ^˘°˛`˙´,.-?:_;>*>#&@\\{}łŁ$ß÷đĐ[]€"
    spec = [*spec]
    for s in spec:
        szo = "".join(szo.split(s))
    return szo
print(szo_tisztitas("hogyan?"))
print(szo_tisztitas("'most!'"))
print(szo_tisztitas("?+='s-z-a-v!a,k@$()'"))

def van_duplavonal(szo):
    szo.split("-")
    
  
print(van_duplavonal("kicsi--nagy"))
# print(van_duplavonal("kicsi--nagy"))
# print(van_duplavonal("")) 
# print(van_duplavonal("magas--"))
# print(van_duplavonal("piros--fekete"))
# print(van_duplavonal("-igen-nem-"))
