# Chess Board

import turtle

t = turtle.Turtle()

t.speed(0)

def drawSquare(color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.rt(90)

    t.end_fill()

t.penup()
t.goto(-200, 200)
t.pendown()

cur_color = "white"

for i in range(8):
    for j in range(8):
        drawSquare(cur_color)
        if cur_color == "white":
            cur_color = "black"

        else:
            cur_color = "white"
        
        t.fd(50)

    if cur_color == "white":
        cur_color = "black"

    else:
        cur_color = "white"
    
    t.penup()
    t.goto(-200, t.ycor()-50)
    t.pendown()
