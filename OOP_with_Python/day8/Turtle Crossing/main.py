from turtle import Turtle,Screen
from traffic import Traffic
import time
from result import Result


timmy=Turtle()
timmy.penup()
timmy.setheading(90)
timmy.goto(0, -280)
timmy.shape("turtle")
timmy.color("dark green")

screen=Screen()

screen = Screen()
screen.setup(800,800)
screen.title("Turtle Crossing Game")
screen.bgcolor("grey")

top_sidewalk = Turtle()
top_sidewalk.shape("square")
top_sidewalk.penup()
top_sidewalk.color("brown")
top_sidewalk.shapesize(stretch_wid=4, stretch_len=60)
top_sidewalk.goto(0, 380)


bottom_sidewalk = Turtle()
bottom_sidewalk.shape("square")
bottom_sidewalk.penup()
bottom_sidewalk.color("brown")
bottom_sidewalk.shapesize(stretch_wid=8, stretch_len=60)
bottom_sidewalk.goto(0, -380)

screen.listen()

screen.tracer(0)

def up():
    timmy.setheading(90)
    timmy.forward(10)
def down():
    timmy.setheading(270)
    timmy.forward(10)
def rt():
    timmy.setheading(0)
    timmy.forward(10)
def left():
    timmy.setheading(180)
    timmy.forward(10)

screen.onkey(rt, "Right")
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

traffic=Traffic()

res=Result()

win=False

while not traffic.collision(timmy):
    time.sleep(0.02)
    screen.update()
    if timmy.ycor()>=340:
        win=True
        break
    traffic.move()

if win==False:
    res.lost()
else:
    res.vict()



screen.exitonclick()