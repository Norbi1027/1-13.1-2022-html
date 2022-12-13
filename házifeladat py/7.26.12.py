import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.left(90)
for i in range(0,4):
    t.forward(100)
    t.right(90)

t.right(45)
t.forward(140)
t.left(75)
t.forward(100)
t.left(120)
t.forward(100)
t.left(75)
t.forward(140)

screen.mainloop()