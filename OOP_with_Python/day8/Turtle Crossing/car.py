from turtle import Turtle

class Car(Turtle):
    def __init__(self,colour):
        super().__init__()
        
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color(colour)
        
        self.car2=Turtle()
        self.car2.penup()
        self.car2.sety(self.ycor())
        self.car2.setx(self.xcor()+200)
        self.car2.shape("square")
        self.car2.setheading(180)
        self.car2.shapesize(stretch_wid=1, stretch_len=4)
        self.car2.color(colour)


