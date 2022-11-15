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
    def mozogj():
        Teknos.forward(20)
        Teknos.left(90)
        Teknos.back(10)
        Teknos.right(90)
        Teknos.forward(10)
        Teknos.left(90)
    def mozogb():
        Teknos.back(10)
        Teknos.right(90)
        Teknos.forward(10)
        Teknos.left(90)



Screen.bgcolor("lightgreen")
Teknos.color("pink")
Teknos.pensize(3)
teknos.rajzol(90,20)
teknos.mozogj()
teknos.rajzol(90,40)
teknos.mozogb()
teknos.rajzol(90,60)
teknos.mozogb()
teknos.rajzol(90,80)
teknos.mozogb()
teknos.rajzol(90,100)

Teknos.back(10)
Teknos.right(90)
Teknos.back(110)

Screen.mainloop()

