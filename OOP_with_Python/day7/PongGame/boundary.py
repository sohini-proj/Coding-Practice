from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()

        # Center circle
        self.center = Turtle()
        self.center.penup()
        self.center.color("white")
        self.center.hideturtle()
        self.center.goto(0, -150)
        self.center.write("o", align="center",font=("Arial", 250, "normal"))

        # Left goal
        self.goal1 = Turtle()
        self.goal1.penup()
        self.goal1.color("white")
        self.goal1.hideturtle()
        self.goal1.goto(-390, -30)
        self.goal1.write("|", align="center",font=("Arial", 70, "normal"))

        # Right goal
        self.goal2 = Turtle()
        self.goal2.penup()
        self.goal2.color("white")
        self.goal2.hideturtle()
        self.goal2.goto(385, -30)
        self.goal2.write("|", align="center",font=("Arial", 70, "normal"))

        # left boundary
        self.lb = Turtle()
        self.lb.shape("square")
        self.lb.color("white")
        self.lb.shapesize(stretch_wid=30, stretch_len=0.5)
        self.lb.penup()
        self.lb.goto(-400,0)

        # right
        self.rb = Turtle()
        self.rb.shape("square")
        self.rb.color("white")
        self.rb.shapesize(stretch_wid=30, stretch_len=0.5)
        self.rb.penup()
        self.rb.goto(392.5,0)

        # up
        self.ub = Turtle()
        self.ub.shape("square")
        self.ub.color("white")
        self.ub.shapesize(stretch_wid=0.5, stretch_len=40)
        self.ub.penup()
        self.ub.goto(0,300)

        # down
        self.db = Turtle()
        self.db.shape("square")
        self.db.color("white")
        self.db.shapesize(stretch_wid=0.5, stretch_len=40)
        self.db.penup()
        self.db.goto(0,-290)
