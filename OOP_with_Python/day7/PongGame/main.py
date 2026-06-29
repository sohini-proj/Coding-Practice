from turtle import Screen
from score import Score
from paddle import Paddle
from boundary import Boundary
from ball import Ball

screen = Screen()
screen.setup(800,600)
screen.bgcolor("dark green")
screen.listen()

score = Score()
boundary=Boundary()

comp = Paddle((-390,20), "black")
player = Paddle((380,20), "blue")

ball=Ball(boundary, comp, player,score)

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")


screen.tracer(0)

while True:
    screen.update()
    ball.move()


screen.exitonclick()