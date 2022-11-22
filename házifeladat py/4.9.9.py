import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("blue")
Screen.bgcolor("lightgreen")
Teknos.speed(10)
Teknos.pensize(1)


def csillag():
    for i in range(0,5):
        Teknos.right(144)
        Teknos.forward(100)

csillag()
Screen.mainloop()