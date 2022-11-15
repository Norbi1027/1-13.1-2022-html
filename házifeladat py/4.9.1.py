import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()

class teknos:

    def rajzol(fok,e):
        for i in range(0,4):
            Teknos.pendown()
            Teknos.forward(e)
            Teknos.left(fok)
            Teknos.penup()

Teknos.pensize(3)
Screen.bgcolor("lightgreen")
Teknos.color("pink")
teknos.rajzol(90,20)
Teknos.back(40)
teknos.rajzol(90,20)
Teknos.back(40)
teknos.rajzol(90,20)
Teknos.forward(120)
teknos.rajzol(90,20)
Teknos.forward(40)
teknos.rajzol(90,20)

Screen.mainloop()
