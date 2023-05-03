import turtle

t = turtle.Turtle()

sides = int(input("Enter how many sides: "))

for i in range(sides):
    t.forward(100)
    t.right(360/sides)
