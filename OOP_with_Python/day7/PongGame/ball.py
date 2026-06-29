from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, boundary, comp, player,score):
        super().__init__()

        self.boundary=boundary
        self.comp=comp
        self.player=player
        self.score=score
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(1)
        self.goto(0, 0)
        self.setheading(random.choice([45, 135, 225, 315]))
        self.comp_score=0
        self.player_score=0



    def change_dir(self):
        self.setheading(360 - self.heading())

    def hit(self):
        self.setheading(180 - self.heading())

    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(random.choice([45, 135, 225, 315]))


    def move(self):

        self.comp.goto(self.comp.xcor(), self.ycor())

        if self.ycor() >= 285:
            self.change_dir()

        if self.ycor() <= -275:
            self.change_dir()

        if self.xcor() <= -370 and abs(self.ycor() - self.comp.ycor()) < 50:
            self.comp_score+=1
            self.hit()

        if self.xcor() >= 360 and abs(self.ycor() - self.player.ycor()) < 50:
            self.player_score+=1
            self.hit()

        if self.xcor() <= -395:
            self.reset_ball()

        if self.xcor() >= 395:
            self.reset_ball()

        self.forward(1)
        self.score.pts(self.comp_score, self.player_score)