import random
#scope

# var defined inside a funtion has local scope
'''
num=36
def increase_num():
    num=40
    print(num)
increase_num()
print(num)
'''

# even if parameterized, var altered in a function does not change a var with global scope
# var val is changed only if function is called. Change is LOCAL
'''
num=4
def increase_num(num):
    num+=2
    print(num)
increase_num(num)
print(num)
'''

# block scope

# Python Does NOT have Block Scope
# any var defined/altered within a block is accessible/changed outside that block too
'''
a,b="",""
if 2>0:
    a="hello"
    b="world"
print(f"[{a} {b}]")
'''

# if fn def after var: after fn is defined, "new_level" will refer to the function not the string
# if var def after fn: error <var can't be called>
'''
game_level=3
new_level="rundown factory"
level=["mystic manor","abandoned caste","spooky graveyard","haunted asylum"]
def new_level():
    if game_level>2:
        index=random.randint(0,3)
        new_level=level[index]
    print(f"new: {new_level}")
print(f"old: {new_level}")
new_level()
'''
# !!!  var names and fn names must be different   !!!
'''
game_level=3
new_level="rundown factory"
level=["mystic manor","abandoned caste","spooky graveyard","haunted asylum"]
def next_level():
    if game_level>2:
        index=random.randint(0,3)
        new_level=level[index]
    print(f"new: {new_level}")
print(f"old: {new_level}")
next_level()
'''


# CODING EXCERCISE

# Prime number checker
"""
    for every possible divisor:
        if divisor works:
            return False
    return True      ---------->  [# We only get here if no divisor worked]
"""
'''
while True:
    print()
    num=int(input("Enter number:"))
    def isprime(num):
        for i in range(2,num-1):
            if num%i==0:
                return False
        return True
    if isprime(num)==True:
        print("prime")
    if isprime(num)==False:
        print("Not prime")
    print()
    ch=input("Do you wanna go agin?(y/n): ")
    if ch=="n":
        break
'''

# print fn -VS- return type
# with "return type" the function ends right after condition is satisfied [does not move to next iteration]

'''
numbers=[1,2,3,4,5,6,7,8,9,10]
# print fn (prints 10 lines)
def isfive():
    for i in numbers:
        if i==5:
            print("is five")
        else:
            print("is not five")
# return type (executes only Untill on of the 1/many conditions is satisfied)
def isfour():
    for i in numbers:
        if i==4:
            return "if four"
        else:
            return "is not four"
    return "number not found"
isfive()
res=isfour()
print(res)
'''


# changing a global variable in local scope

a=5
def inc():
    global a
    a+=2
    print(a)
inc()
print(a)