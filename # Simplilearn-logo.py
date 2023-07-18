# Simplilearn-logo
import turtle

window = turtle.Screen()
t = turtle.Turtle()
t = turtle.Pen()

t.speed(0.01) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

window.bgcolor("#154360")

t.begin_fill()
t.color("orange")
for i in range(4):
    t.forward(20)
    t.right(90)
t.end_fill()

t.up()
t.goto(0,-40)
t.down()

t.begin_fill()
t.color("orange")
for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(150)
    t.right(90)
t.end_fill()

t.up()
t.goto(50,75)
t.down()

t.begin_fill()
t.color("#3498DB")
for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(190)
    t.right(90)
t.end_fill()

t.up()
t.goto(-50,75)
t.down()

t.begin_fill()
t.color("orange")
for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(190)
    t.right(90)
t.end_fill()

