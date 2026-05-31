#===========================================================================================
#                                         DAY 3
#===========================================================================================

#functions with params
def heading():
    print("===========================================================================================")
    print("                                         DAY 3")
    print("===========================================================================================")
heading()
def greet(x):
    print("Hello "+x)
    print("Let's get started")
greet("Andrea")

# example: calculating num of weeks left till age 90
def calcweeks(age):
    print(f"You have {(90-age)*52} weeks left")
age=int(input("Enter your age: "))
calcweeks(age)

# switch param positions will still result in correct positioning is same names are used and arguments specified
def sum(a,b):
    print(f"sum of {a} and {b} is {a+b}.")
a=8
b=1
sum(b,a)
sum(b=1,a=8)

