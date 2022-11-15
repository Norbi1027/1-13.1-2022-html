import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("blue")
Screen.bgcolor("lightgreen")
Teknos.speed(1)

class rajzol:
    def csiga(elore,szog,x):
        for i in range(0,x):
            Teknos.forward(elore+(i+i))
            Teknos.left(szog)
rajzol.csiga(10,90,147)
Screen.mainloop()
