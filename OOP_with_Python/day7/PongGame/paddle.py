from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()

        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 80)

    def down(self):
        if self.ycor() > -226:
            self.goto(self.xcor(), self.ycor() - 80)