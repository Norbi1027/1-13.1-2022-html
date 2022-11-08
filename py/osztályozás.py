import random

x=random.randint(0,100)
print("Százalék száma:",x,"%")

if x<51:
    print("Ez sajnos egyes :(")

if x>=50 and x<61:
    print("Ez egy kettecske lesz")

if x>=60 and x<71:
    print("Ez egy hármas lesz")

if x>=70 and x<81:
    print("Ez egy négyes lesz")

if x>80:
    print("Ötööös")
