import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("blue")
Screen.bgcolor("lightgreen")
Teknos.pensize(2)

Teknos.left(90)
class rajzol:
    def negyzet(elore,szög,szor):
        for x in range(0,szor):
            Teknos.speed(10)
            Teknos.right(15)
            for i in range(0,4):
                Teknos.forward(elore)
                Teknos.right(szög)

rajzol.negyzet(100,90,24)
Screen.mainloop()



