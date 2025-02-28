import turtle
import random

from turtle import *
screen= turtle.Screen()
screen. setup (800,450)
screen.bgcolor ("brown" )

Turtle()
speed (0)
color ("white")
penup()
goto (-350,180)
pendown ( )
fillcolor ("green")
begin_fill()
for i in range (2):
    forward(700)
    right (90)
    forward (350)
    right (90)
end_fill()
ht()

heading= turtle.Turtle()
heading.pencolor("white") 
heading.speed(0)
heading.penup()
heading.goto(0,180)
heading.write("Turtle Race", align="center", font= ("monospace", 30))

p1=turtle.Turtle()
p1.shape ("turtle") 
p1.color ("orange")
p1.shapesize (2.0,2.0)
p1.penup()
p1.goto (-300,150)

p2=turtle.Turtle()
p2.shape ("turtle")
p2.color ("blue")
p2.shapesize (2.0,2.0)
p2.penup ()
p2.goto (-300,50)

p3=turtle.Turtle()
p3.shape ("turtle")
p3.color ("red")
p3.shapesize (2.0,2.0)
p3.penup()
p3.goto (-300, -50)

p4=turtle.Turtle()
p4.shape ("turtle") 
p4.color ("black") 
p4. shapesize (2.0,2.0)
p4.penup()
p4.goto (-300, -150)

finishline=turtle.Turtle()
finishline.pensize(3)
finishline.pencolor("black")
finishline.penup()
finishline.goto(280,180)
finishline.right(90)
finishline.pendown()
finishline.forward(350)
finishline.hideturtle()

result= turtle.Turtle()
result.pencolor("white") 
result.speed(0)
result.penup()
result.goto(0,-210)
result.hideturtle()


while p1.xcor() <= 280 and p2.xcor() <= 280 and p3.xcor() <= 280 and p4.xcor() <= 280:
    p1.forward(random.randint(1,10))
    p2.forward(random.randint(1,10))
    p3.forward(random.randint(1,10))
    p4.forward(random.randint(1,10))

if p1.xcor() > p2.xcor() and p1.xcor() > p3.xcor()and p1.xcor() > p4.xcor():
    print("P1 won the game")
    result.write("P1 Won the game", align="center", font= ("monospace", 30))
    for i in range(55):
        p1.right(10)
elif p2.xcor() > p1.xcor() and p2.xcor() > p3.xcor()and p2.xcor() > p4.xcor():
    print("P2 won the game")
    for i in range(55):
        p2.right(10)
    result.write("P2 Won the game", align="center", font= ("monospace", 30))
elif p3.xcor() > p1.xcor() and p3.xcor() > p2.xcor()and p3.xcor() > p4.xcor():
    print("P3 won the game")
    for i in range(55):
        p3.right(10)
    result.write("P3 Won the game", align="center", font= ("monospace", 30))
else:
    print("P4 won the game") 
    for i in range(55):
        p4.right(10)
    result.write("P4 Won the game", align="center", font= ("monospace", 30))
screen.mainloop()
