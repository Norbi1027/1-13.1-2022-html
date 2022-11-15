import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

screen.bgcolor("lightgreen")
teknos.color("darkblue")

teknos.shape("turtle")
# 360 / 12 = 30
teknos.pensize(3)

for i in range(0,12):
   teknos.penup()
   teknos.forward(100)
   teknos.pendown()
   teknos.forward(20)
   teknos.penup()
   teknos.forward(20)
   teknos.stamp()
   teknos.forward(-140)
   teknos.left(30)

screen.mainloop()