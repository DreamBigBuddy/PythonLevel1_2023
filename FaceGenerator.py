# Face Generator

import turtle

def draw_face(face_size, face_color, eye_size, eye_color, mouth_size, mouth_color):
    t.color(face_color)
    t.begin_fill()
    t.circle(face_size)
    t.end_fill()
    
    t.pu()
    t.goto(-eye_size*2, eye_size*6.5)
    t.pd()

    t.color(eye_color)
    t.begin_fill()
    t.circle(eye_size)
    t.end_fill()

    t.pu()
    t.goto(eye_size*2, eye_size*6.5)
    t.pd()

    t.color(eye_color)
    t.begin_fill()
    t.circle(eye_size)
    t.end_fill()

    t.pu()
    t.goto(-mouth_size, mouth_size*1.5)
    t.pd()
    t.rt(90)

    t.color(mouth_color)
    t.begin_fill()
    t.circle(mouth_size, 180)
    t.end_fill()

    t.hideturtle()

face_size = int(input("Size of Face: "))
face_color = input("Color of Face: ")
eye_size = int(input("Size of Eyes: "))
eye_color = input("Color of Eyes: ")
mouth_size = int(input("Size of Mouth: "))
mouth_color = input("Color of Mouth: ")

t = turtle.Turtle()
t.speed(0)

draw_face(face_size, face_color, eye_size, eye_color, mouth_size, mouth_color)
