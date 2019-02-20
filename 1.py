import turtle
import math
 
screen = turtle.getscreen()
 
#turtle.forward(100)
#turtle.right(120)
#turtle.forward(100)
#turtle.right(120)
#turtle.forward(100)
#turtle.right(120)
 
def sidedFigure(zijdes, groote):
  for squareSide in range(zijdes):
    turtle.forward(groote)
    turtle.left(360 / zijdes)
 
 
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.goto(0, 200)
 
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.goto(-200, 0)
 
turtle.penup()
 
turtle.color("red")
for x in range (31):
  x = x - 15
  turtle.goto(x * 5, pow(x, 2) - 10)
  turtle.pendown()
 
turtle.penup()
 
turtle.color("yellow")
for x in range (31):
  turtle.goto(x * 10, math.sqrt(x) + 15)
  turtle.pendown()
 
#sidedFigure(360, 2)
