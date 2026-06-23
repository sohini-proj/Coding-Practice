import random
from turtle import Turtle,Screen

print("""
======================================================================================================
                                    🐢  T U R T L E   R A C E  🐢
======================================================================================================

                                        WELCOME TO THE TRACK!

RULES:
--------------------------------------------------------
1. Six turtles will compete in a race.

2. Before the race starts, place your bet by entering the turtle's colour.

3. Possible choices:
      🟢 green
      🟡 yellow
      🔴 red
      🔵 blue
      🩷 pink
      ⚫ black
""")
    
is_race_on=False

screen=Screen()
screen.setup(500,400)
user_guess=screen.textinput(title="Make your BET !",prompt="Which Turtle will win the race? (enter colour): ")
print(user_guess)

line=Turtle()
line.hideturtle()
line.color("red")
line.penup()
line.goto(220,90)
line.pendown()
line.goto(220,-100)


timmy=Turtle()
timmy.shape("turtle")

colours=["green","yellow","red","blue","pink","black"]
y_pos=[70,40,10,-20,-50,-80]
all_turtles=[]

for i in range(6):
    timmy=Turtle()
    timmy.penup()
    timmy.shape("turtle")
    timmy.color(colours[i])
    timmy.goto(-220,y_pos[i])
    timmy.speed(random.choice([1,3,6,10]))
    all_turtles.append(timmy)


if user_guess:
    is_race_on=True


while is_race_on:
    for i in all_turtles:
        dist=random.randint(0,10)
        i.forward(dist)
        if i.xcor() >=220:
            col=i.color()
            is_race_on=False
            break

print("""
====================================================================================================================
      
                                               !!!  RESULT  !!!

====================================================================================================================
""")

if col[0] == user_guess:
    print(" YOU WON !!!!")

else:
    print(f"Wompwompwomp Better luck next time.\nThe winner was {col[0]}")



screen.exitonclick()