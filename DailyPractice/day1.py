
print("Day one of documented practice!")
'''
#type casting to boolean 1=True, 0=False
print(bool(1))

#type casting to determine number of letters in a name
print("num of letters in ur name: "+str(len(input("enter ur first name: "))))
'''
'''
#program to calculate, round(to 2 decimal places) and display bmi USING F-STRING
h=float(input("enter height in meters: "))
w=float(input("enter weight in kgs: "))
bmi=w/(h**2)
print(f"BMI: {bmi}\nRounded BMI: {round(bmi,2)}")

#program to calculate tip and split bill
bill=float(input("Enter bill amount: "))
per=float(input("tip percentage(10%/12%/15%): "))
n=int(input("Enter number of people: "))
amt = (bill+(bill*(per/100)))/n
print("each person pays: ",amt)
'''
'''
#amusement park ticket price calculator
#first checks height then age then whether or not they want a picture
h=float(input("enter height in cm: "))
age=int(input("enter age: "))
photo=input("do you want a photo?(y/n): ")
p=0

if h<120:
    print("Sorry, NOT eligible for this ride")
else:
    if age<5:
        p+=5
    elif 5<=age<=12:
        p+=7
    else:
        p+=10
    if photo=="y":
        p+=3

print("amt to pay with 10% tax: $",p+(p*0.1))
'''
'''
#pizza order system S,M,L=$15,$20,$25; toppings:cost extra;
while True:
    print("!!! WELCOME TO PYTHON PIZZA DELIVERY EXPRESS !!!")
    print("~~~~~~~~~~~~~~ BUILD UR OWN PIZZA ~~~~~~~~~~~~~~")
    print("\n")
    print("CHOOSE A SIZE:\n1. Small    ~$15\n2. Medium   ~$20\n3. Large    ~$25 ")
    ch=int(input("ENTER CHOICE(1,2,3): "))
    print("\n")
    print("NOW ADD YOUR CHOICE OF TOPPINGS:\n1. Extra Cheese   ~$1\n2. Pepperoni      ~$3\n3. Veggies        ~$4\n4. Pineapple      ~$2.5\n5. Paneer         ~$5")
    top=input("ENTER TOPPINGS SELECTED: ")
    print("\n")
    

    p=0
    if ch==1:
        p+=15
    elif ch==2:
        p+=20
    else:
        p+=25

    for i in top:
        if i in ["1","2","3","4","5"]:
            if i=="1":
                p+=1
            if i=="2":
                p+=3
            if i=="3":
                p+=4
            if i=="4":
                p+=2.5
            if i=="5":
                p+=5
    print("Item total amt: $",p)
    print("Payable amt with 10% tax: $",p+p*0.1)

    op=input("Do you want to place another order?(y/n): ")
    if op=="n":
        break
    if op!="n" and op!="y":
        print("INVALID I/P. back to main...")
'''
import random
numero=random.randint(5,10)
print(numero)

