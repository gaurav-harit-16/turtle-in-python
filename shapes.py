import turtle
import random
t=turtle.Turtle()
t.hideturtle()
t.pensize(2)

turtle.colormode(255)
def tcolor():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    t.color(a, b, c)

def sq(x):
    t.fd(x)
    for i in range(3):
        t.left(90)
        t.fd(x)
    t.left(90)

def un(x):
    t.fd(x)
    t.left(60)
    t.fd(x)
    t.left(120)
    t.fd(x)
    t.left(60)
    t.fd(x)
    t.left(120)

def hx(x):
    t.fd(x)
    for i in range(5):
        t.left(60)
        t.fd(x)
    t.left(60)
wn=turtle.Screen()
wn.bgcolor("black")

t.speed(0)

def p1():
    for i in range(20):
        tcolor()
        sq(150)
        t.left(145)
def p2():
    for i in range(110):
        tcolor()
        sq(150)
        t.left(177)
def p3():
    for i in range(20):
        for j in range(8):
            tcolor()
            un(15+15*i)
            t.left(45)
def p4():
    for i in range(10):
        for j in range(4):
            tcolor()
            hx(100)
            t.left(15)
def cr(x):
    t.circle(x)
    t.left(45)



def clr():
    t.clear()

wn.listen()

t.speed(0)
wn.onkey(p1, "Up")
wn.onkey(p2, "Down")
wn.onkey(p3, "Right")
wn.onkey(p4, "Left")

wn.onkey(clr, "space")
turtle.mainloop()
