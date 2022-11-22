import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("blue")
Screen.bgcolor("lightgreen")
Teknos.speed(10)
Teknos.pensize(10)


def haromszog(t,sz):
    for i in range(0,3):
        t.forward(200)
        t.left(sz)

haromszog(Teknos,120)
Screen.mainloop()
