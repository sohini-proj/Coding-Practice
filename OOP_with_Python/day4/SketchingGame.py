from turtle import Turtle,Screen

print("""
==================================================================================================================
      
==============================================================================================================

███████╗████████╗ ██████╗██╗  ██╗     █████╗ ███╗   ██╗██████╗     ███████╗██╗  ██╗███████╗████████╗ ██████╗██╗  ██╗
██╔════╝╚══██╔══╝██╔════╝██║  ██║    ██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝██╔════╝██║  ██║
█████╗     ██║   ██║     ███████║    ███████║██╔██╗ ██║██║  ██║    ███████╗█████╔╝ █████╗     ██║   ██║     ███████║
██╔══╝     ██║   ██║     ██╔══██║    ██╔══██║██║╚██╗██║██║  ██║    ╚════██║██╔═██╗ ██╔══╝     ██║   ██║     ██╔══██║
███████╗   ██║   ╚██████╗██║  ██║    ██║  ██║██║ ╚████║██████╔╝    ███████║██║  ██╗███████╗   ██║   ╚██████╗██║  ██║
╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝

                                      D R A W   •   M O V E   •   C R E A T E

==============================================================================================================

RULES / CONTROLS

→ Arrow Keys      : Face a direction
→ SPACEBAR        : Draw forward by 10 steps
→ TAB             : Move forward without drawing
→ R               : Rotate clockwise by 5°
→ L               : Rotate anti-clockwise by 5°

OBJECTIVE

Use the turtle as your digital pen.
Create any drawing you like using movement + direction controls.

No score.
No timer.
Just vibes.

==============================================================================================================

==================================================================================================================
""")

timmy=Turtle()
timmy.shape("turtle")
timmy.color("dark blue","dark green")

screen=Screen()
screen.setup(width=900, height=700)
screen.bgcolor("beige")
screen.title("ETCH & SKETCH")

timmy.width(5)

# use of setheading() fn to face a cerain angle

def rt():
    timmy.setheading(0)

def left():
    timmy.setheading(180)

def up():
    timmy.setheading(90)

def down():
    timmy.setheading(270)

def r():
    timmy.right(5)

def l():
    timmy.left(5)

def draw():
    timmy.forward(10)
def move():
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.listen()
screen.onkey(rt,"Right")
screen.onkey(left,"Left")
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(draw,"space")
screen.onkey(move,"Tab")
screen.onkey(r,"r")
screen.onkey(l,"l")


screen.exitonclick()