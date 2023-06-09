# Smiley Face

import turtle

t = turtle.Turtle()

t.speed(0)

t.begin_fill()
t.color("yellow")
t.circle(100)
t.end_fill()

t.pu()
t.goto(-35, 125)
t.pd()

t.color("black")

t.begin_fill()
t.circle(20)
t.end_fill()

t.pu()
t.goto(35, 125)
t.pd()

t.begin_fill()
t.circle(20)
t.end_fill()

t.pu()
t.goto(-50, 75)
t.pd()

t.pensize(10)

t.rt(90)

t.circle(50, 180)
