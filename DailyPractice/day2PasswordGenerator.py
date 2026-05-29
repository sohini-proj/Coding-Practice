import random

let=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=[0,1,2,3,4,5,6,7,8,9]
sym=['~','!','@','#','$','%','^','&','*','(',')','-','_']

while True:
    passlet=[]
    passnum=[]
    passsym=[]
    passw=[]
    password=[]
    print("\n")
    print("---------- PYTHON ALPHA-NUMERIC PASSWORD GENERATOR ----------")
    print("\n")

    l=int(input("How many LETTERS would you like your password to have?: "))
    n=int(input("How many NUMBERS would you like your password to have?: "))
    s=int(input("How many SPECIAL CHARACTERS would you like your password to have?: "))
    print("\n")
    for i in range(0,l):
        passlet.append(random.choice(let))
        i+=1
    for i in range(0,n):
        passnum.append(random.choice(num))
        i+=1
    for i in range(0,s):
        passsym.append(random.choice(sym))
        i+=1
    passw=[passlet,passnum,passsym]
    for i in passw:
        for j in i:
            password.append(str(j))
    for i in range(0,10):
        random.shuffle(password)
        i+=1
    newpass="".join(password)
    print(newpass)
    print("\n")
    
    ch=input("Do you wanna generate another?(y/n): ")
    if ch=="n":
        break


    