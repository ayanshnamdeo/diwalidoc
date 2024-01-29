# import turtle
# t = turtle.Turtle()
# turtle.Screen().setup(500, 550)
# turtle.Screen().bgcolor('black')
# t.pencolor('blue')
# t.fillcolor('orange')
# t.begin_fill()
# t.pensize(8)
# t.speed(10)
# t.right(60)
# t.forward(200)
# t.goto(0, 0)
# t.right(60)
# t.forward(200)
# t.left(80)
# t.circle(160, 78)
# t.end_fill()
# def set_position(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
# t.pensize(10)
# set_position(-25, -40)
# t.right(60)
# t.circle(60, 48)
# set_position(-43, -70)
# t.right(60)
# t.circle(75, 68)
# set_position(15, -170)
# t.pensize(8)
# t.circle(30)
# def star():
#     t.pensize(2)
#     t.pencolor('red')
#     t.fillcolor('yellow')
#     t.begin_fill()
#     for i in range(5):
#         t.forward(30)
#         t.right(144)
#     t.end_fill()
#     t.pensize(10)
#     t.pencolor('red')
# def curly_star(setheading, circle_x, circle_y):
#     set_position(0, 10)
#     t.setheading(setheading)
#     t.circle(circle_x, circle_y)
#     star()
# def straight_star(setheading, forward):
#     set_position(0, 10)
#     t.setheading(setheading)
#     t.forward(forward)
#     star()
# curly_star(145, 75, 60)
# curly_star(120, 150, 60)
# curly_star(95, 200, 60)
# straight_star(90, 200)
# curly_star(85, -200, 60)
# curly_star(60, -150, 60)
# curly_star(35, -75, 60)
# # Writing "Happy Diwali" at the bottom
# set_position(0, -270)
# t.pencolor('pink')
# t.write('Happy Diwali', align='center', font=('Arial', 30,))
# # Adding a star at the bottom
# set_position(0, -290)
# star()
# def draw_firework(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     for _ in range(36):
#         t.color("orange")
#         t.forward(50)
#         t.right(170)
# # Set up the turtle
# t = turtle.Turtle()
# turtle.Screen().bgcolor('black')
# t.speed(10)
# # Draw fireworks in each corner
# draw_firework(-200, 200)
# draw_firework(200, 200)
# draw_firework(-200, -200)
# draw_firework(200, -200)
# t.hideturtle()
# turtle.done()


import turtle
import random
import time

# You have to create your own window to run each drawing command. You can do this by initializing variables.

t = turtle.Turtle()
s = turtle.Screen()

# Setting up the screen’s height and width (Here we have both height and width equals to 1 so, we will get a full screen.)

s.setup(width=1.0, height=1.0)
s.colormode(255)

# Giving screen a background colour

turtle.Screen().bgcolor("Black")

# setting colour of pen

t.pencolor('yellow')

# speed refers to the speed of the pen here, 0 is the max speed and 1 is minimum speed.
t.speed(0)

# This will help us to hide the cursor of the turtle.
t.hideturtle()

# This determines the width of the pen.
t.pensize(4)

# This will create a rangoli design for our animation.
'''This function will create 10 circles,
and each time radius will be reduced to radius-4 '''


def draw(radius):
    for i in range(10):
        t.circle(radius)
        radius = radius-4


'''This function will call draw function 10 times
    and everytime the turtle will change its direction'''


def design():
    for i in range(10):
        draw(120)
        t.right(36)
    t.penup()


design()


# This function will create a rocket cracker.
def rocket():

    t.hideturtle()
    # setting position of the head of the rocket which is a triangle
    t.setpos(-510, -180)
    t.color('yellow')  # colour of the outine of the head
    t.pendown()
    t.begin_fill()  # this will fill the colour in triangle shape(head).
    for count in range(3):
        t.fd(50)
        t.lt(120)
    t.end_fill()
    t.penup()  # stops drawing on the screen.
    t.pendown()  # This will again start drawing
    '''This will create a rectangle shape
        as the body of the rocket'''
    t.color('red')
    t.begin_fill()
    t.fd(50)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(80)
    t.end_fill()
    t.penup()
    t.setpos(-470, -350)
    t.speed(0)
    '''This will create the stick of the rocket'''
    t.pendown()
    t.color('brown')
    t.begin_fill()
    t.fd(100)
    t.rt(90)
    t.fd(2)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(2)
    t.end_fill()
    t.penup()
    t.penup()
    t.setpos(-495, -283)
    t.speed(0)
    t.pensize(3)

    '''This will draw the part where we lit'''
    t.pendown()
    t.color('brown')
    t.begin_fill()
    t.fd(3)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(3)
    t.rt(90)
    t.fd(20)
    t.end_fill()
    t.penup()
    t.pendown()

    '''This will create a fire like structure at the rocket'''
    Radius = 10
    t.pensize(1)
    x_coord = (-500)
    y_coord = (-290)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('yellow')
    for i in range(5):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(20)


rocket()


# Function to draw crackers

def crackers():
    # it randomly selects radius between the given values
    Radius = random.randint(80, 180)
    x_coord = (400)
    y_coord = (350)
    t.penup()
    t.setpos(x_coord, y_coord)  # sets the position of the cracker's center
    t.pendown()
    t.pencolor('blue')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (360)
    y_coord = (250)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('red')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (560)
    y_coord = (130)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('pink')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (-360)
    y_coord = (180)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('orange')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (-480)
    y_coord = (120)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('purple')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(70, 120)
    x_coord = (-530)
    y_coord = (380)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('yellow')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(50, 100)
    x_coord = (540)
    y_coord = (350)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('orange')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (-530)
    y_coord = (150)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('green')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)


crackers()
# Functions to display HAPPY DIWALI


def h():
    t.penup()
    t.setpos(-300, 200)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(180)
    t.fd(100)


def a1():
    t.penup()
    t.setpos(-200, 200)
    t.pendown()
    t.left(90)
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(180)
    t.fd(50)
    t.right(60)
    t.fd(50)


def p1():
    t.penup()
    t.setpos(-50, 200)
    t.pendown()
    t.left(150)
    t.fd(80)
    t.right(180)
    t.circle(25)


def p2():
    t.penup()
    t.setpos(50, 200)
    t.pendown()
    t.left(180)
    t.fd(80)
    t.right(180)
    t.circle(25)


def y():
    t.penup()
    t.setpos(150, 200)
    t.pendown()
    t.left(150)
    t.fd(110)
    t.right(180)
    t.fd(60)
    t.right(120)
    t.fd(60)
    t.right(180)
    t.fd(60)
    t.right(60)
    t.fd(50)
    t.left(120)


def d():
    t.penup()
    t.setpos(-350, -300)
    t.pendown()
    t.left(90)
    t.fd(100)
    t.right(90)
    t.circle(-50, 180, 30)
    t.right(180)


def i1():
    t.penup()
    t.setpos(-250, -300)
    t.pendown()
    t.fd(50)
    t.left(180)
    t.fd(25)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(25)
    t.backward(50)


def w():
    t.penup()
    t.setpos(-150, -200)
    t.pendown()
    t.right(90)
    t.fd(100)
    t.left(135)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.left(135)
    t.fd(100)
    t.right(180)
    t.fd(100)


def a2():
    t.penup()
    t.setpos(-50, -300)
    t.pendown()
    t.left(90)
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(180)
    t.fd(50)
    t.right(60)
    t.fd(50)


def l():
    t.penup()
    t.setpos(100, -300)
    t.pendown()
    t.left(150)
    t.fd(100)
    t.right(180)
    t.fd(100)
    t.left(90)
    t.fd(60)


def i2():
    t.penup()
    t.setpos(200, -300)
    t.pendown()
    t.fd(50)
    t.left(180)
    t.fd(25)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(25)
    t.backward(50)


t.setheading(0)
t.color("white")
t.pensize(10)

h()
a1()
p1()
p2()
y()
d()
i1()
w()
a2()
l()
i2()
t.hideturtle()

time.sleep(2)
t.penup()

# And our program is ready!!! Let's run it and see the output
turtle.done