import turtle
from pygame import mixer

t = turtle.Turtle()
turtle.Screen().bgcolor("black")

t.penup()
t.goto(-230, 175)
t.pendown()

mixer.init()
mixer.music.load("titanic.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

turtle.delay(40)

t.pencolor("white")
t.pensize(15)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(170)
t.right(90)
t.forward(50)
t.backward(100)

t.penup()
t.goto(0, 0)
t.pendown()

t.color("red")
t.begin_fill()
t.right(130)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

t.penup()
t.goto(140, 175)
t.pendown()

t.pencolor("white")
t.right(40)
t.forward(120)
t.circle(60, 180)
t.forward(120)

t.penup()
t.goto(-220, -150)
t.pendown()
t.write("Faisal Shafique", font=("Arial",50,"bold"))

t.hideturtle()
turtle.done()
