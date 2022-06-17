import turtle
import random

screen=turtle.Screen()
t=turtle.Turtle()
list1=["yellow","green","blue","red","purple","pink","orange"]
# t.hideturtle()
# turtle.dot()

# turtle.fd(50)
# turtle.dot(20, "blue")
# turtle.fd(50)

# t.position()
# t.color("blue")
# astamp=t.stamp()
# t.fd(50)
# t.position()
# t.clearstamp(astamp)

# for i in range(10):
#     t.fd(50)
#     t.stamp()
# t.clearstamps(2)
# t.clearstamps(-2)
# t.clearstamps()


# for i in range(5):
#     t.fd(50)
#     t.lt(80)
# t.undo()
# t.undo()
# for i in range(5):
#     t.undo()

# t.goto(100,100)

# t.home()
# t.left(50)
# t.forward(100)
# print(t.pos())
# print(round(t.xcor(), 5))#round is to get input in decimal round(number,ndigit(how many decimals))
# print(round(t.ycor(), 5))
# print(t.xcor())
# t.fd(50)
# t.degrees(2)
t.speed(1)

# t.shape("circle")
# t.shapesize(5,2)
# t.tilt(30)
# t.tilt(30)
# t.tilt(30)
# t.tilt(30)
# t.tilt(30)
# t.tilt(30)


# t.resizemode("user")
# t.shapesize(5, 5, 15)
# t.fd(200)

# t.shape("circle")
# t.shapesize(5,2)
# t.shearfactor(5)
# t.settiltangle(45)
# t.fd(50)
# t.settiltangle(-80)
# t.fd(50)
# t.settiltangle(45)
# t.fd(50)
# t.settiltangle(-80)
# t.fd(50)

# t.shape("square")
# t.shapesize(5,2)
# t.shapetransform(4,-1,0,2)
# t.get_shapepoly()
# print(t.get_shapepoly())


def up():
    t.setheading(90)
    t.fd(100)

def down():
    t.setheading(270)
    t.fd(100)

def left():
    t.setheading(180)
    t.fd(100)

def right():
    t.setheading(0)
    t.fd(100)

def rightc(x,y):
    t.color(random.choice(list1))

def leftc(x,y):
    t.stamp()



screen.listen()



turtle.mainloop()
