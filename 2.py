import turtle
import random
 
rnd = random.randint
 
turtle.speed(0)
 
def drawRect(corners, size, width, rotation, positionx, positiony, r, g, b):
  turtle.penup()
 
  turtle.color(r,g,b)
 
  turtle.goto(positionx, positiony)
 
  turtle.left(rotation)
 
  turtle.width(width)
 
  turtle.pendown()
 
  for x in range(corners):
    turtle.forward(size)
    turtle.left(360 / corners)
 
for y in range(35):
  drawRect(rnd(3, 8), rnd(5, 150), rnd(1, 5), rnd(0, 360), rnd(-250, 250), rnd
(-250, 250), rnd(0, 255), rnd(0,255), rnd(0,255))
