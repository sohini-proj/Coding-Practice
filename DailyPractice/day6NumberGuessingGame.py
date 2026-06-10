import random

print("""
 _   _ _   _ __  __ ____  _____ ____         ____ _   _ _____ ____ ____ ___ _   _  ____ 
| \ | | | | |  \/  | __ )| ____|  _ \       / ___| | | | ____/ ___/ ___|_ _| \ | |/ ___|
|  \| | | | | |\/| |  _ \|  _| | |_) |      | |  _| | | |  _| \___ \___ \| ||  \| | |  _
| |\  | |_| | |  | | |_) | |___|  _ <       | |_| | |_| | |___ ___) |__) | || |\  | |_| |
|_| \_|\___/|_|  |_|____/|_____|_| \_\       \____|\___/|_____|____/____/___|_| \_|\____|

                                ____    _    __  __ _____
                               / ___|  / \  |  \/  | ____|
                              | |  _  / _ \ | |\/| |  _|
                              | |_| |/ ___ \| |  | | |___
                               \____/_/   \_\_|  |_|_____|
""")

while True:
    print("\n   LEVELS   \n\n1. EASY [10 chances]\n2. HARD [5 chances]")
    level=input("Enter level(1,2):")
    print()
    print("Number is between 0 and 100\n~~~ ALL THE BEST ~~~\n")
    if level=="1":
        list=[]
        for i in range(10):
            n=random.randint(0,100)
            list.append(n)
        num=random.choice(list)
        i=10
        print(f"You have {i} chances to guess:\n")
        while (i>0):
            i-=1
            ip=int(input("Enter number: "))
            if ip==num:
                print("yayyyyyy U guessed it right")
                break
            elif ip<num:
                if num-ip>=30:
                    print(f"Toooo less\nU've got {i} more chance(s)\n")
                elif num-ip in range(10,30):
                    print(f"Less. Guess higher\nU've got {i} more chance(s)\n")
                elif num-ip in range(0,10):
                    print(f"Less but close. Guess a little higher\nU've got {i} more chance(s)\n")
            elif ip>num:
                if ip-num>=30:
                    print(f"Toooo High\nU've got {i} more chance(s)\n")
                elif ip-num in range(10,30):
                    print(f"High. Guess Lower\nU've got {i} more chance(s)\n")
                elif ip-num in range(0,10):
                    print(f"High but close. Guess a little lower\nU've got {i} more chance(s)\n")
            else:
                print(f"INVALID INPUT\nU've got {i} more chance(s)\n")
        print(f"Number was: {num}")
    elif level=="2":
        list=[]
        for i in range(10):
            n=random.randint(0,100)
            list.append(n)
        num=random.choice(list)
        i=5
        print(f"You have {i} chances to guess:\n")
        while (i>0):
            i-=1
            ip=int(input("Enter number: "))
            if ip==num:
                print("yayyyyyy U guessed it right")
                break
            elif ip<num:
                if num-ip>=30:
                    print(f"Toooo less\nU've got {i} more chance(s)\n")
                elif num-ip in range(10,30):
                    print(f"Less. Guess higher\nU've got {i} more chance(s)\n")
                elif num-ip in range(0,10):
                    print(f"Less but close. Guess a little higher\nU've got {i} more chance(s)\n")
            elif ip>num:
                if ip-num>=30:
                    print(f"Toooo High\nU've got {i} more chance(s)\n")
                elif ip-num in range(10,30):
                    print(f"High. Guess Lower\nU've got {i} more chance(s)\n")
                elif ip-num in range(0,10):
                    print(f"High but close. Guess a little lower\nU've got {i} more chance(s)\n")
            else:
                print(f"INVALID INPUT\nU've got {i} more chance(s)\n")
        print(f"Number was: {num}") 
    else:
        print("INVALID INPUT\n")

    ch=input("Do you wanna go again?(y/n): ")
    if ch=="n":
        break
        
