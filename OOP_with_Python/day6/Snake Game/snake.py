import turtle

starting_pos = [(0, 0), (-10, 0), (-20, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in starting_pos:
            t = turtle.Turtle()
            t.penup()
            t.shape("square")
            t.shapesize(0.5, 0.5)
            t.goto(pos)
            t.color("white")
            self.segments.append(t)

    def face(self, screen):
        def rt():
            if self.segments[0].heading() != 180:
                self.segments[0].setheading(0)

        def left():
            if self.segments[0].heading() != 0:
                self.segments[0].setheading(180)

        def up():
            if self.segments[0].heading() != 270:
                self.segments[0].setheading(90)

        def down():
            if self.segments[0].heading() != 90:
                self.segments[0].setheading(270)

        screen.onkey(rt, "Right")
        screen.onkey(left, "Left")
        screen.onkey(up, "Up")
        screen.onkey(down, "Down")

    def new(self):
        num = len(self.segments) - 1
        t = turtle.Turtle()
        t.penup()
        t.shape("square")
        t.shapesize(0.5, 0.5)

        d = self.segments[num].heading()
        pos = list(self.segments[num].pos())

        if d == 0.0:
            pos[0] -= 10
        elif d == 180.0:
            pos[0] += 10
        elif d == 90.0:
            pos[1] -= 10
        elif d == 270.0:
            pos[1] += 10

        t.goto(pos[0], pos[1])
        t.setheading(d)
        t.color("white")
        self.segments.append(t)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        self.segments[0].forward(10)