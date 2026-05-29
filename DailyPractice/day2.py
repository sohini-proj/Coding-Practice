import random
import math
'''
#for a number in a given range, includes both a and b in(a,b)
a=random.randint(0,10)
print(a)

#random.random() [w/o any params] is for a number in range (0,1)
b=random.random() * 100
print(b)

#for floating point numbers that may include both a and b in range (a,b)
c=random.uniform(3,7)
print(c)

#heads or tails game
n=random.randint(0,100)
print("number generated: ",n)
if n%2==0:
    print("HEAD")
else:
    print("TAIL")
'''

#LISTS
'''
fruits=["apple","mango","cherry","orange"]
print(fruits[1]," ",fruits[-1])

#to add at end
fruits.append("banana")
print(fruits[-1])

#to add at desired index (index,item)
fruits.insert(1,"strawberry")
print(fruits[1])

#to change cherry--->cherries
fruits[3]="cherries"
print(fruits)

#to add a buch of items
fruits.extend(["dragon fruit","passion fruit","raspberries"])
print(fruits)

# to remove item "x" --> list.remove(x)
fruits.remove("banana")

# to remove val @index"i" --> list.pop(i)
fruits.pop(2)
print(fruits)
'''
#Nested Lists
'''
l1=[1,2,3]
l2=[4,5,6]
l3=[l1,l2]
print(l3)
'''

# EXCERCISE: Who will pay the bill?
# option 1: using random.choice()
'''
while True:
    print("\nENTER THE NAMES OF FRIENDS")
    names=[]
    i=1
    while True:
        print("\n")
        n=input(f"Enter the name of friend {i}: ")
        names.append(n)
        i+=1
        ch=input("Do you Want to add a name?(y,n): ")
        if ch=="n":
            break
    print("\n")
    print("list of names: ",names)
    print("\n")
    print("Person that will pay is ",random.choice(names),"!")
    print("\n")
    op=input("Wanna go again?(y/n): ")
    if op=="n":
        break
'''
#option2: using random.randint()
'''
while True:
    print("\nENTER THE NAMES OF FRIENDS")
    names=[]
    i=1
    while True:
        print("\n")
        n=input(f"Enter the name of friend {i}: ")
        names.append(n)
        i+=1
        ch=input("Do you Want to add a name?(y,n): ")
        if ch=="n":
            break
    print("\n")
    s=len(names)
    index=random.randint(0,s-1)
    print("list of names: ",names)
    print("\n")
    print("Person that will pay is ",index,"!")
    print("\n")
    op=input("Wanna go again?(y/n): ")
    if op=="n":
        break
'''
"""
rock='''
        _______
_______|   ____)_
          (______)
          (_______)
          (______)
----------(______)

'''
paper='''
         _________
________|      ___)______
                 ________)_
                 __________)
                __________)
--------<_______________)

'''
scissor='''
           ________
__________|     ___)______
                 _________)_
           _____ ___________)
          (______)
----------(______)

'''
"""
# sum and max of elements of a list
'''
scores=[120,123,111,99,145,147,139,91,119,149]
sum=0
max=0
for i in scores:
    sum+=i
    i+=1
print(f"SUM of all scores is {sum}")
num=len(scores)
for i in range(0,num):
    if scores[i]>max:
        max=scores[i]
    i+=1
print(f"The largest score is {max}")
'''
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)


