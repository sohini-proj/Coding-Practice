import random

c1='''
 __________
|          |
|          
|         
|         
|__

'''

c2='''
 __________
|          |
|          O
|         
|         
|__

'''

c3='''
 __________
|          |
|          O
|         /
|         
|__

'''

c4='''
 __________
|          |
|          O
|         /|
|         
|__

'''

c5='''
 __________
|          |
|          O
|         /|\\
|         
|__

'''

c6='''
 __________
|          |
|          O
|         /|\\
|         / 
|__

'''
c7='''
 __________
|          |
|          O
|         /|\\
|         / \\
|__
=========================================================
                       GAME OVER
=========================================================
'''
words = ["python", "castle", "treasure", "dragon", "adventure", "mystery", "pirate", "jungle", "wizard", "galaxy", "thunder", "warrior", "volcano", "diamond", "kingdom", "shadow", "monster", "phoenix", "labyrinth", "island"]
print("=========================================================")
print("\n------------ WELCOME TO PYTHON HANGMAN GAME ------------\n")

while True:
    print("=========================================================")
    listman=[c1,c2,c3,c4,c5,c6,c7]
    word=random.choice(words)
    listw=[]
    for i in word:
        listw.append(i)

    nlet=len(word)

    s=""
    for i in range(nlet):
        s+="_"

    l1=[]
    for i in s:
        l1.append(i)
    print("".join(l1))

    while len(listman)!=0:
        print("\n")
        user=input("enter letter: ")
        print("\n")
        if user in word:
            for i in range(nlet):
                if word[i]==user:
                    l1[i]=word[i]
                    print("".join(l1))
            if l1==listw:
                print('''
                    =========================================================
                                            YOU WON!!!
                    =========================================================
                ''')
                break
        else:
            print(listman[0])
            listman.pop(0)
    print("\n")
    print("Original word: ",word)
    ch=input("Wanna go again?: ")
    print("\n")
    if ch=="n":
        break
    


