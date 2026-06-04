#===========================================================================================
#                                         DAY 3
#===========================================================================================

#functions with params
def heading():
    print("===========================================================================================")
    print("                                         DAY 3")
    print("===========================================================================================")
heading()
'''
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
'''

# DICTIONARIES
'''
dict1={"apple":"red","banana":"yellow","lemon":"green"}
print(dict1["apple"])
print(dict1.keys())
dict1["lemon"]="lime"
print(dict1)
dict1["cherry"]="cola-red"
print(dict1)
'''
# iterating through dictionaries gives KEY not VALUE
'''
names={1:"billy",2:"jason",3:"atlanta"}
for i in names:
    print(i)
    print(names[i])
'''
# adding updated elements to a new dictionary
'''
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def grade(n):
    if n in range(91,101):
        return "Outstanding"
    if n in range(81,91):
        return "Exceeds Expectations"
    if n in range(71,81):
        return "Acceptable"
    if n <= 70:
        return "Fail"

student_grades = {}
for i in student_scores:
    student_grades[i]=grade(student_scores[i])
print(student_grades)
'''
# NESTING in Dictionaries
d={
    "India":{
        "Delhi":["Red Fort","India Gate"],
        "Mumbai":["Marine Drive","Gateway of India"]
    },
    "China":{
        "Beijing":["Forbidden Palace","Tiannmen Square"],
        "Chongqing":["Train station"]
    }    
}
print(d.keys())
print(d["India"])
print(d["China"])
print(d[India][Delhi])
print(d[India][Delhi][1])




