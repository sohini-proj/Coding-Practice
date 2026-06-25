from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        # Scoreboard
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)


    def pts(self, comp, player):
        self.clear()
        self.write(f"Score: {comp} | {player}",align="center", font=("Arial", 15, "normal"))