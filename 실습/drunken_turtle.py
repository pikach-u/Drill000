import turtle
import random

turtle.shape('turtle')
while(True):
    turtle.setheading(random.randint(0,60))
    turtle.forward(random.randint(10,20))
    turtle.stamp()
