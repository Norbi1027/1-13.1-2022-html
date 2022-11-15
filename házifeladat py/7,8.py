import turtle

screen = turtle.Screen()
szögek = [160, -43, 270, -97, -43, 200, -940, 17, -86]
kalóz = turtle.Turtle()
végsőSzög = 0

for szög in szögek:
   turtle.left(szög)
   turtle.forward(100)
   végsőSzög = végsőSzög + szög

done = True
while done:
   if végsőSzög > 360:
      végsőSzög = végsőSzög - 360
   elif végsőSzög < 0:
      végsőSzög = végsőSzög + 360
   else:
      done = False



print(f"A kalóz {végsőSzög} fokba néz.")