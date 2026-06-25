from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, boundary):
        super().__init__()

        self.boundary = boundary
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(1)
        self.goto(0, 0)
        self.setheading(random.choice([45, 135, 225, 315]))
        self.penalty = 0

    def change_dir(self):
        self.setheading(360 - self.heading())

    def hit(self):
        self.setheading(180 - self.heading())

    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(random.choice([45, 135, 225, 315]))

    def move(self):

        if self.ycor() >= 285:
            self.change_dir()
            self.forward(1)
            return

        if self.ycor() <= -275:
            self.change_dir()
            self.forward(1)
            return

        if self.xcor() <= -385:
            self.hit()
            self.forward(1)
            return

        if self.xcor() >= 380:
            self.reset_ball()
            self.penalty += 1
            return

        self.forward(1)