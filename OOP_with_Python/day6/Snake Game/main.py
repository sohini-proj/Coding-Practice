from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

print("""
                            ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗
                            ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝
                            ███████╗██╔██╗ ██║███████║█████╔╝ █████╗
                            ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝
                            ███████║██║ ╚████║██║  ██║██║  ██╗███████╗
                            ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

                                        ██████╗  █████╗ ███╗   ███╗███████╗
                                        ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                                        ██║  ███╗███████║██╔████╔██║█████╗
                                        ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
                                        ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                                        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝


                            ━━━━━━━━━━━━━━━━ RULES ━━━━━━━━━━━━━━━━

                            ► Use ARROW KEYS to control the snake

                            ► Eat the RED FOOD to grow longer

                            ► Each food eaten increases your score

                            ► Do NOT hit the walls

                            ► Do NOT collide with your own body

                            ► Survive as long as possible

                            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                                    PRESS ENTER TO START
""")

screen = Screen()
screen.setup(600, 600)
screen.listen()
screen.tracer(0)

screen.bgcolor("black")
screen.title("MY SNAKE GAME")

timmy = Snake()
food = Food()
score = Score()
score.start()

screen.update()
timmy.face(screen)
screen.update()


game_started = False

def start():
    global game_started
    game_started = True

screen.onkey(start, "Return")

while not game_started:
    screen.update()

game_on = True
score.starttxt.clear()

while game_on:
    screen.update()
    time.sleep(0.1)

    timmy.move()

    if timmy.segments[0].distance(food) < 15:
        food.refresh()
        score.inc_score()
        timmy.new()

    if timmy.segments[0].xcor()>290 or timmy.segments[0].xcor()<-290 or timmy.segments[0].ycor()>290 or timmy.segments[0].ycor()<-290:
        game_on=False
        score.game_over()
    for i in timmy.segments:
        if i == timmy.segments[0] or  i == timmy.segments[1]:
            pass
        elif timmy.segments[0].distance(i) < 10:
            game_on=False
            score.game_over()

    

screen.exitonclick()