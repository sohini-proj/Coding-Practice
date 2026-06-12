
recipe={
    "espresso":[50,0,18],
    "latte":[200,150,24],
    "cappuccino":[250,100,24]
}
stock={
    "water":1250,
    "milk":750,
    "coffee":125
}
def reduce_stock(item):
    list=recipe[item]
    n=0
    for i in stock:
        for j in list:
            num=list.index(j)
            if n==num:
                stock[i]-=j
        n+=1
reduce_stock("espresso")
print(stock)
def espresso(money):
    if money<1.50:
        print(f"\nInsufficient change.\n${money} refunded.\n")
    else:
        reduce_stock("espresso")
        print(f"Here is your coffee.")
        change=1.50-money
        print(f"Here is your change of ${change}.")
        return stock
new=espresso(200)
espresso(200)
print(new)