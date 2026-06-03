while True:
    print("\n")
    print("--------------- Welcome To The Python Bidding Game ---------------")
    print("\n")
    bids={}
    q=input("Are You ready to bid?(y/n): ")
    if q=="n":
        break
    while True:
        print("\n"*100)
        name=input("Enter bidder Name: ")
        print("\n")
        amt=float(input("Enter bid: $"))
        print("\n")
        bids[name]=amt
        ch=input("Are there any other bidders?(y/n): ")
        if ch=="n":
            break
    max=0
    winner=""
    for key in bids:
        if bids[key]>max:
            winner=key
            max=bids[key]
    print("\n"*100)
    print("The winner of this bid is: ",winner)
    print("With a bid of $",max)
    print("\n")
    op=input("Do you wanna bid once more?(y/n): ")
    if op=="n":
        break
