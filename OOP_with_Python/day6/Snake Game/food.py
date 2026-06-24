from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.4,0.4)
        self.penup()
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        self.goto(x,y)
