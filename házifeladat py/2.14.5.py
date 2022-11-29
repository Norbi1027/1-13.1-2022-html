c = 10000  
r = 0.08    
m = 12 
t = int(input("Írd be hány évre szeretnéd a kamatozást: "))
fv = (c * ((1 + r / m) ** (m * t)))

print("A betét értéke:", fv)