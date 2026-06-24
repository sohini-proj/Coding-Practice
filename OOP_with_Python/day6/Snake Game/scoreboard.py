from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.s = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.update()
        self.starttxt=Turtle()
        self.starttxt.penup()
        self.starttxt.hideturtle()
        self.starttxt.color("white")


    def start(self):
         self.starttxt.goto(0,180)
         self.starttxt.write(f"PRESS ENTER TO START", align="center", font=("Arial", 15, "normal"))
         

    def update(self):
        self.write(f"Score: {self.s}", align="center", font=("Arial", 15, "normal"))

    def inc_score(self):
        self.s+=1
        self.clear()
        self.update()

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "normal"))