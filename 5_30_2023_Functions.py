# Functions

import turtle

t = turtle.Turtle()

def printName():
   print("Hi Vaman!")

printName()

def add(x, y):
   print(x + y)

add(5, 10)

def drawSquare(side_length):
    for i in range(4):
        t.forward(side_length)
        t.right(90)

drawSquare(100)

t.circle(50, 180)
