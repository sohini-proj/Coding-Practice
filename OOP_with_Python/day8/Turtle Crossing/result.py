from turtle import Turtle

class Result(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def vict(self):
        self.color("green")
        self.write("YAYYYY !!! YOU WON !!!", align="center",font=("Arial", 40, "normal"))

    def lost(self):
        self.color("red")
        self.write("GAME OVERRR",align="center",font=("Arial", 40, "normal"))