import random

# range(a,b) has range [a,b-1]
#random.randint(a,b) has range [a,b]

dice_face=[1,2,3,4,5,6]
dice_num=random.randint(1-1,6-1)      #for range [0,5] as "b" is considered in randint fn
print(dice_num)

# CODING EXCERCISE
# Generation identification
'''
def generation(year):
    if year in range(1883,1901):
        return "belong to the Silent Generation"
    if year in range(1901,1928):
        return "belong to the Silent Generation"
    if year in range(1928,1946):
        return "belong to the Silent Generation"
    if year in range(1946,1965):
        return "are a Baby Boomer"
    if year in range(1965,1981):
        return "belong to Generation X"
    if year in range(1981,1997):
        return "are a Millenial"
    if year in range(1997,2013):
        return "are a Gen-Z"
    if year in range(2013,2025):
        return "are Gen-Alpha"
    if year in range(2015,2027):
        return"are Gen-Beta"
    
print("""

                         ____ _____ _   _ _____ ____      _  _____ ___ ___  _   _
                        / ___| ____| \ | | ____|  _ \    / \|_   _|_ _/ _ \| \ | |
                       | |  _|  _| |  \| |  _| | |_) |  / _ \ | |  | | | | |  \| |
                       | |_| | |___| |\  | |___|  _ <  / ___ \| |  | | |_| | |\  |
                        \____|_____|_| \_|_____|_| \_\/_/   \_\_| |___\___/|_| \_|

                         ___ ____  _____ _   _ _____ ___ _____ ___  _____  ___
                        |_ _|  _ \| ____| \ | |_   _|_ _|  ___|_ _|| ____||  _ \\
                         | || | | |  _| |  \| | | |  | || |_   | | |  _|  | |_) |
                         | || |_| | |___| |\  | | |  | ||  _|  | | | |___ |  _ <
                        |___|____/|_____|_| \_| |_| |___|_|   |___||_____||_| \_\\

""")

while True:
    print("\nEnter your age to find out which generation you belong to!!!\n")
    n=(input("Enter your AGE / YEAR of birth: "))
    num=int(n)
    if len(n)==2 or len(n)==3:
        age=num
        year=2026-age
    if len(n)==4:
        year=num
        age=2026-year
    
    gen=generation(year)
    print()
    print(f"You were born in the year {year} and are {age} year(s) old as off 2026.\nSo you {gen} !")
    print()
    ch=input("Another try?(y/n): ")
    if ch=="n":
        break
'''

# ERROR HANDLING
# catching exceptions with "try" and "except" blocks

# Voting eligibility checker
'''
while True:
    print()
    while True:
        try:
            age=int(input("Enter age: "))
            break
        # except block only executes if error has occured
        except ValueError:
            print("Invalid Input. Try entering a numerical value such as 18. \n")

    if age>=18:
        print("\nYou are eligible to vote\n")
    else:
        print("\nNot eligible to vote.\n")
    ch=input("Another try?(y/n): ")
    if ch=="n":
        break
'''

# DEBUGGING

# Excercise_1: Odd or Even

#def odd_or_even(number):
#   if number % 2 = 0:
#       return "This is an even number."
#   else:
#       return "This is an odd number."

'''
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
while True:
    print()
    num=float(input("enter number: "))
    print()
    print(odd_or_even(num))
    print()
    ch=input("Do you wanna go again?(y/n): ")
    if ch=="n":
        break
'''

# Excercise_2: 

#def is_leap(year):
#   if year % 4 == 0:
#       if year % 100 == 0:
#           if year % 4000 == 0:
#               return True
#           else:
#               return False
#       else:
#           return True
#   else:
#       return False
'''
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(is_leap(2000))
'''

# Excercise_3:
# Target is the number up to which we count
#def fizz_buzz(target):
#   for number in range(1, target + 1):
#       if number % 3 == 0 or number % 5 == 0:
#           print("FizzBuzz")
#       if number % 3 == 0:
#           print("Fizz")
#       if number % 5 == 0:
#           print("Buzz")
#       else:
#           print([number])

# Target is the number up to which we count
'''
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(10)
'''