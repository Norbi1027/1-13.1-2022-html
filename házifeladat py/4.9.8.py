import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("blue")
Screen.bgcolor("lightgreen")
Teknos.speed(10)
Teknos.pensize(3)

Teknos.left(90)
def kor(r):
    for i in range(0,36):
        Teknos.forward(r)
        Teknos.right(10)

kor(20)
Screen.mainloop()