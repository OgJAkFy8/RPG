import turtle
from random import randint
from randomColor import * #randname
##


## Funtions

def equallines(size):
    t.backward(size)
    t.up()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.down()
    t.forward(size)


def dtriangle(size):
        t.down()
        for i in range(3):
            t.right(120)
            t.forward(size+(i*2))
        t.up()

def filledCircle(size):
    t.fillcolor(listname(i))
    t.down()
    t.begin_fill()
    t.right(size*20)
    t.circle(size)
    t.end_fill()
    t.up()


def filledsquare(size):
    t.fillcolor(listname(size))
    t.down()
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.forward(size)
    t.end_fill()
    t.up()


# User Variables
screen_x = 400
screen_y = 401



# Turtle Setup
t=turtle.Pen()
t.shape()
t.reset()
screen = turtle.Screen()
screen.screensize(screen_x, screen_y)


## Begin Program -
equallines(100)
print(screen_x,' ',screen_y)

for i in range(12):
    t.setpos(180,-1*i)
    t.circle(40, 270)
    dtriangle(123+i)
    t.forward(90+i)
    filledsquare(i*8)
    t.forward(150-i)
    filledCircle(i*3)
    t.setpos(-180+i,-170)
    t.setheading(90+i)
    filledCircle(11*randint(2,7))
