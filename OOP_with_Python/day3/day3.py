from turtle import Turtle,_Screen
import turtle as t
import random

timmy=Turtle()

our_screen=_Screen()

timmy.shape("turtle")
timmy.color("dark blue","dark green")
'''
# draw a square
for i in range(4):
    timmy.right(90)
    timmy.forward(200)

timmy.reset()

# draw a pentagon
for i in range(5):
    timmy.right(72)
    timmy.forward(200)

timmy.reset()

# draw a star
for i in range(5):
    timmy.forward(200)
    timmy.right(144)

timmy.reset()

# draw dashed line  [using penup() and pendown() functions to lift the cursor and move forward without drawing anything]
timmy.penup()
timmy.setx(-250)
for i in range(50):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)

timmy.reset()

# concentric polygons
angles=[120,90,72,60,51.42857,45,40]
vibgyor=["dark violet","dark blue","light blue","green","yellow","orange","red"]
index=0
for i in range(3,10):
    timmy.color(vibgyor[index],"dark green")
    for j in range(i):
        timmy.right(angles[index])
        timmy.forward(70)
    index+=1

timmy.reset()

# random walk
timmy.pensize(5)
direction=["front","back","rt","left"]
def get_colour():
    colours=[]
    for i in range(25):
        ind=random.randint(0,6)
        colours.append(vibgyor[ind])
    num=random.randint(0,24)
    return colours[num]
def get_dir():
    new_dir=[]
    for i in range(15):
        ind=random.randint(0,3)
        new_dir.append(direction[ind])
    num=random.randint(0,14)
    return(new_dir[num])
def move(dir,col):
    timmy.color(col,"dark green")
    if dir=="front":
        timmy.forward(15)
    elif dir=="back":
        timmy.right(180)
        timmy.forward(15)
    elif dir=="rt":
        timmy.right(90)
        timmy.forward(15)
    else:
        timmy.left(90)
        timmy.forward(15)
timmy.speed("fastest")
for i in range(200):
    col=get_colour()
    dir=get_dir()
    move(dir,col)
timmy.speed(6)
'''

# custom colours after changing colourmode to 255 

t.colormode(255)

# random walk with randomized colours

timmy.pensize(5)
direction=["front","back","rt","left"]
def get_colour():
    list=[]

    for i in range(3):
        l=[]
        l2=[]
        l3=[]
        for j in range(100):
            num=random.randint(0,255)
            l.append(num)
        for k in range(50):
            num2=random.choice(l)
            l2.append(num2)
        for a in range(10):
            num3=random.choice(l2)
            l3.append(num3)
        ele=random.choice(l3)
        list.append(ele)
    return tuple(list)

def get_dir():
    new_dir=[]
    for i in range(15):
        ind=random.randint(0,3)
        new_dir.append(direction[ind])
    num=random.randint(0,14)
    return(new_dir[num])

def move(dir,col):
    timmy.color("dark green")
    timmy.pencolor(col)
    if dir=="front":
        timmy.forward(15)
    elif dir=="back":
        timmy.right(180)
        timmy.forward(15)
    elif dir=="rt":
        timmy.right(90)
        timmy.forward(15)
    else:
        timmy.left(90)
        timmy.forward(15)
'''
timmy.speed("fastest")
for i in range(200):
    col=get_colour()
    dir=get_dir()
    move(dir,col)
timmy.speed(6)
'''

# spirograph

timmy.pensize(1)
angle=5
timmy.speed("fastest")
for i in range(int(360/angle)+1):
    timmy.pencolor(get_colour())
    timmy.circle(100)
    timmy.right(angle)


_Screen.exitonclick()