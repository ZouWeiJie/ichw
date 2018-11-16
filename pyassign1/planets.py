import math
import turtle
sun = turtle.Turtle()
mer = turtle.Turtle()
ven = turtle.Turtle()
ear = turtle.Turtle()
mar = turtle.Turtle()
jup = turtle.Turtle()
sat = turtle.Turtle()

colors=[ 'yellow','blue', 'lime', 'red', 'black','orange','aqua']    

def orbit(turtle,x,y,m,n,d,size,k):        
    if m == 0:
        turtle.shape("circle")
        turtle.shapesize(size)
        turtle.color(colors[k])
        turtle.up()
        turtle.goto(d+x,0)

        turtle.down()
        turtle.showturtle()
    else:

        turtle.speed(0)
        m =5*m/n
        turtle.shape("circle")
        turtle.shapesize(size)
        turtle.color(colors[k])
        turtle.goto(d+x*math.cos(math.radians(m)),y*math.sin(math.radians(m)))
for i in range(10000):
    orbit(sun,0,0,i,8,0,1.50,0)
    orbit(mer,29,19,i,0.28,-4,0.12,1)
    orbit(ven,54,53.6,i,0.8,0,0.3,2)
    orbit(ear,75,72,i,1.2,0,0.3,3)
    orbit(mar,114,92,i,2.32,9,0.167,4)
    orbit(jup,190,172,i,14.4,15,0.9,5)
    orbit(sat,280,254,i,25.6,22,0.7,6)
