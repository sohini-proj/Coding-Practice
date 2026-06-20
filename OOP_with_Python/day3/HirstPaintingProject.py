from turtle import Turtle,_Screen
import turtle as t
import random

timmy=Turtle()

our_screen=_Screen()

num=int(input("Enter square grid size: "))

timmy.shape("turtle")
timmy.color("dark blue","dark green")

t.colormode(255)

def get_col():
    l=[]
    for i in range(3):
        l.append(random.randint(0,255))
    return(tuple(l))
def draw(num):
    for i in range(num):
        for j in range(num):
            timmy.dot(15, get_col())
            timmy.penup()
            timmy.forward(50)
        timmy.penup()
        timmy.setx(-250)
        timmy.right(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.pendown()
timmy.penup()
timmy.goto(-250,200)
timmy.pendown()

draw(num)



_Screen.exitonclick(self)