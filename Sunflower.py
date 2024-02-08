from turtle import *
from math import *

speed (150)
bgcolor("black")
goto(0, -40)

for i in range(16):
    for j in range(18):
        color('#00B374')
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
    circle(40,24)

color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_angle=137.508

phi = golden_angle*(pi/180)

for i in range(110):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup()
    goto(x,y)
    setheading(i*golden_angle)
    pendown()
    stamp()

done()