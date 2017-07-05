import turtle

def door():
    # Create screen and turtle.
    screen = turtle.Screen()
    
    screen.title('Square Demo')
    screen_x, screen_y = 300,400 #screen.screensize()
    t=turtle.Pen()
    """
    Draws a border around the canvas in red.
    """
    # Lift the pen and move the turtle to the center.
    t.penup()
    t.home()

    # t.penup()
    t.home()
    t.right(90)
    t.forward(screen_y / 2)
    t.left(90)
    t.forward(100)
    t.pencolor('green')
    
    t.hideturtle()
    t.pendown()
    t.pensize(3)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(150)
    t.setheading(180)
    t.penup()
    t.forward(10)
    t.right(90)
    t.setheading(180)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.left(90)

    t.penup()
    t.forward(150)

    t.pendown()
    for i in range(4):
        t.forward(100)
        t.left(90)

    t.penup()
    t.left(180)
    t.forward(20)
    t.pendown()
    t.color("black", "red")
    t.begin_fill()
    t.pencolor('red')
    t.circle(6)
    t.end_fill()
    


door()
