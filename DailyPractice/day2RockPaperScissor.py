import random

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
game=[rock,paper,scissor]
while True:
    print("\n")
    print("!!! WELCOME TO PYTHON ROCK PAPER SCISSOR !!!")
    print("\n")
    print("ROCK = 0\nPAPER = 1\nSCISSOR = 2\n")
    user=int(input("Enter Choice (0/1/2): "))
    print("\n")
    comp=random.randint(0,2)
    if user==0:
        print("YOU:")
        print(rock)
        print("Computer:")
        if comp==0:
            print(rock)
            print("Result: DRAW!")
        if comp==1:
            print(paper)
            print("Result: wompwomp YOU LOST ")
        if comp==2:
            print(scissor)
            print("Result: YAYYY YOU WON !!! ")
    elif user==1:
        print("YOU:")
        print(paper)
        print("Computer:")
        if comp==0:
            print(rock)
            print("Result: YAYYY YOU WON !!! ")
        if comp==1:
            print(paper)
            print("Result: DRAW!")
        if comp==2:
            print(scissor)
            print("Result: wompwomp YOU LOST ")
    elif user==2:
        print("YOU:")
        print(scissor)
        print("Computer:")
        if comp==0:
            print(rock)
            print("Result: wompwomp YOU LOST ")
        if comp==1:
            print(paper)
            print("Result: YAYYY YOU WON !!! ")
        if comp==2:
            print(scissor)
            print("Result: DRAW! ")
    else:
        print("INVALID INPUT")
    print("\n")
    ch=input("wanna try again??(y/n): ")
    if ch=="n":
        break