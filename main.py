from turtle import *

screen = Screen()

screen.title("Write Your Name")
screen.bgcolor("black")
screen.setup(width= 1000, height=1000)

yertle = Turtle()

yertle.pensize(3)
yertle.speed(4)

def move(x, y):
    yertle.pu()
    yertle.goto(x, y)
    yertle.pd()

def M(x, y):
    yertle.color("red")
    move(x, y)
    yertle.setheading(90)
    yertle.forward(100)
    yertle.right(150)
    yertle.forward(60)
    yertle.left(120)
    yertle.forward(60)
    yertle.right(150)
    yertle.forward(100)


def A(x, y, placeholder):
    yertle.color(placeholder)
    move(x, y)
    yertle.setheading(75)
    yertle.forward(100)
    yertle.right(150)
    yertle.forward(100)
    yertle.backward(50)
    yertle.right(100)
    yertle.forward(25)

def H(x, y):
    yertle.color("orange")
    move(x+40, y)
    yertle.setheading(90)
    yertle.forward(100)
    yertle.backward(50)
    yertle.right(90)
    yertle.forward(40)
    yertle.left(90)
    yertle.forward(50)
    yertle.backward(100)
    
def D(x, y):
    yertle.color("grey")
    move(x, y)
    yertle.setheading(90)
    yertle.forward(100)
    yertle.setheading(0)
    yertle.circle(-50, 180)

def I(x, y):
    yertle.color("white")
    move(x, y)
    move(x-30, y)
    yertle.setheading(0)
    yertle.forward(70)
    yertle.backward(35)
    yertle.setheading(90)
    yertle.forward(100)
    yertle.setheading(0)
    yertle.forward(30)
    yertle.backward(60)

def R(x, y):
    move(x, y)
    yertle.color("blue")
    yertle.setheading(90)
    yertle.forward(100)
    yertle.right(90)
    yertle.circle(-25, 180)
    yertle.left(135)
    yertle.forward(70)


M(-300, 0)
A(-220, 0, "green")
H(-185,0)
D(-80,0)
I(0, 0)
A(50, 0, "pink")
R(125, 0)
screen.exitonclick()