import math
import turtle
def planet(turtle,size,n):
    if size < 1.5 :
        turtle.hideturtle()
    colors=[ 'yellow','blue', 'lime', 'red', 'black','orange','aqua']
    turtle.shape("circle")
    turtle.shapesize(size)
    turtle.color(colors[n])
    turtle.speed(0)
def orbit(turtle,x,y,m,n,d):
    if m == 0:
        turtle.up()
        turtle.goto(d+x*math.cos(math.radians(1)),y*math.sin(math.radians(1)))
        turtle.down()
        turtle.showturtle()
    else:
        m = m/n
        turtle.goto(d+x*math.cos(math.radians(m)),y*math.sin(math.radians(m)))
sun=turtle.Turtle() 
planet(sun,1.50,0)
mer=turtle.Turtle() 
planet(mer,0.12,1)
ven=turtle.Turtle()
planet(ven,0.3,2)
ear=turtle.Turtle() 
planet(ear,0.3,3)
mar=turtle.Turtle()
planet(mar,0.168,4)
jup=turtle.Turtle() 
planet(jup,0.9,5)
sat=turtle.Turtle() 
planet(sat,0.7,6)
for i in range(10000):
    orbit(mer,29,19,i,0.035,-4)
    orbit(ven,54,53.6,i,0.1,0)
    orbit(ear,75,72,i,0.15,0)
    orbit(mar,114,92,i,0.29,9)
    orbit(jup,190,172,i,1.8,15)
    orbit(sat,280,254,i,3.2,22)
