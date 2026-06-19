import copy

recipe={
    "espresso":[50,0,18],
    "latte":[200,150,24],
    "cappuccino":[250,100,24]
}

price={
    "espresso":1.50,
    "latte":2.50,
    "cappuccino":3.00
}

stock={
    "water":1250,
    "milk":750,
    "coffee":125
}

def reduce_stock(item):
    list=recipe[item]
    n=0
    for i in report:
        for j in list:
            num=list.index(j)
            if n==num:
                report[i]-=j
        n+=1
    return report



# we cant just use stock.copy() as both dicts will point to the same inner lists
# to copy the lists as well
#   1. import copy
#   2. use deepcopy() fn ---->  report = copy.deepcopy(stock)

report=copy.deepcopy(stock)

def refill():
    return copy.deepcopy(stock)


def calc_money():
    p=float(input("Enter number of pennies ($0.01): "))
    n=float(input("Enter number of nickels ($0.05): "))
    d=float(input("Enter number of dimes ($0.10): "))
    q=float(input("Enter number of quarters ($0.25): "))
    return p*0.01 + n*0.05 + d*0.10 + q*0.25

def espresso(money):
    if money<1.50:
        return f"\nInsufficient change.\n${money} refunded.\n",report
    
    else:
        reduce_stock("espresso")
        change=money-1.50
        return f"Here is your change of ${change:.2f}\nEnjoy your espresso!",report
    

def latte(money):
    if money<2.50:
        return f"\nInsufficient change.\n${money} refunded.\n",report
    
    else:
        reduce_stock("latte")
        change=money-2.50
        return f"Here is your change of ${change:.2f}\nEnjoy your latte!",report
    

def cappuccino(money):
    if money<3.00:
        return f"\nInsufficient change.\n${money} refunded.\n",report
    
    else:
        reduce_stock("cappiccino")
        change=money-3.00
        return f"Here is your change of ${change:.2f}\nEnjoy your cappuccino!",report
    
    
while True:
    print("""
====================================================================================================================
                                ( (
                                 ) )
                              ........         C O F F E E   M A C H I N E
                              |      |             Brew • Sip • Repeat
                              \\      /
                               `----'
====================================================================================================================
""")
    print("\n MENU OPTIONS")
    print("""
   CHOICE OF OPTIONS
    1. ESPRESSO         ~ $1.50
    2. LATTE            ~ $2.50
    3. CAPPUCCINO       ~ $3.00
          
   CHOICE OF OPERATIONS (STAFF)
    4. VIEW STOCK
    5. REFILL
          
    """)
    ch=int(input("Enter choice of operation (1/2/3/4/5): "))
    print()
    if ch==1:
        money=calc_money()
        output,report=espresso(money)
        print(output)
    if ch==2:
        money=calc_money()
        output,report=latte(money)
        print(output)
    if ch==3:
        money=calc_money()
        output,report=cappuccino(money)
        print(output)
    if ch==4:
        print("Stock available for use:")
        print(report)
    if ch==5:
        report=refill()
        print(report)
        print("Stock refilled.")
    print()
    op=input("Do you want to select another operation?(y/n): ")
    if op=="n":
        break


