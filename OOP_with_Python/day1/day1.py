import demo

n=demo.name
a=demo.age

print(n,"\n",a)

# using turtle module

# importing only "Turtle" class
'''
from turtle import Turtle
jimjam=Turtle()
'''
import turtle
# with CLASS "Turtle"  by importing WHOLE class
#creating an object "Timmy" the turtle
'''
timmy = turtle.Turtle()           # from class Turtle
print(timmy)

# using another class "Screen" in turtle

my_screen=timmy.screen                  # set-up screen
print(my_screen.canvheight)             # print height of screen (300 here)

timmy.shape("turtle")                   # giving obj "timmy" a shape
timmy.color("dark green","green")       # making timmy green

timmy.left(200)
timmy.forward(100)

my_screen.exitonclick()                 # set screen to exit only on a click [present at the end coz exec stops]
'''

# working with Pretty table  [needed to use pip and install]
'''
try:
    import prettytable  # pyright: ignore[reportMissingImports]
    print("done")
except ImportError:
    prettytable = None
'''

import prettytable as pt

table=pt.PrettyTable()
print(table)

table.add_column("S_ID",["101","102","103","104","105","106"])      # add_column( <coln_name>, [<list_of_values/ele])
table.add_column("NAME",["Anne","Billy","Candice","Dylan","Esther","Fiona"])
table.add_column("MARKS",["87.63","88.52","91.01","73.78","79.81","93.07",])
print(table)

table._left_padding_width=0
table.align="l"
print(table)