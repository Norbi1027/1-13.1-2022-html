import turtle



Screen = turtle.Screen()

Teknős = turtle.Turtle()



class teknos:

    def Rajzol(hányszor, fok):

        Screen.clear()

        Teknős = turtle.Turtle()

        for x in range(0, hányszor):



            Teknős.left(fok)

            Teknős.forward(100)



Screen = turtle.Screen()

Teknős = turtle.Turtle()



teknos.Rajzol(3,120)

teknos.Rajzol(4,90)

teknos.Rajzol(6,60)

teknos.Rajzol(8,45)



Screen.mainloop()