from turtle import *

screen = Screen()

screen.title("Write Your Name")
screen.bgcolor("black")
screen.setup(width= 1000, height=500)

yertle = Turtle()

yertle.pensize(3)
yertle.speed(3)

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


def A(x, y):
    yertle.color("green")
    move(x, y)
    yertle.circle(20)
    move(x+40, y)
    yertle.setheading(90)
    yertle.forward(40)









M(-300, 0)
A(-200, 0)


screen.exitonclick()