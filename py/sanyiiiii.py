import turtle
def tobbszinu_negyzet_rajzolas(t, h):
    for i in["white", "pink", "hotpink", "red"]:
        t.speed(1000)
        t.color(i)
        t.forward(h)
        t.left(90)

a = turtle.Screen()
a.bgcolor("black")

Eszti = turtle.Turtle()
Eszti.pensize(3)

meret = 20
for i in range(150):
    tobbszinu_negyzet_rajzolas(Eszti, meret)
    meret = meret + 10
    Eszti.forward(5)
    Eszti.right(9)  
  
a.mainloop()