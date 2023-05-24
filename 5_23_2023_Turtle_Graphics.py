# Graphics

import turtle

t = turtle.Turtle()

t.speed(0)

t.color("blue")
t.fillcolor("green")

t.begin_fill()
t.circle(50, 360, 8)
t.end_fill()

t.penup()
t.goto(200, 200)
t.pendown()

t.color("black")
t.fillcolor("red")

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()
