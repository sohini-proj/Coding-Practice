import random

print(
    '''
 _____________
|             |                  ___                ___
|  A __  __   |                 |___)  |     /_\\  |    |_/
|   (  \/  )__|__________       |____) |___ /   \\ |___ | \\
|    \    /|             |                    _____       ___
|     \  / | K    /\     |                      |  /_\\  |    |_/
|      \/  |     /  \    |                    __| /   \\ |___ | \\
|          |    /    \   |
|          |    \    /   |
|__________|     \  /    |
           |      \/     | 
           |           K |
           |_____________|  

'''
)

cards={
    "spades":["Ace",2,3,4,5,6,7,8,9,10,"jack","king","queen"],
    "diamonds":["Ace",2,3,4,5,6,7,8,9,10,"jack","king","queen"],
    "hearts":["Ace",2,3,4,5,6,7,8,9,10,"jack","king","queen"],
    "clubs":["Ace",2,3,4,5,6,7,8,9,10,"jack","king","queen"]
}

def extractval(card,tot):
    if type(card)==int:
        val=card
        name=card
    else:
        if card in ["jack","king","queen"]:
            val=10
            name=card
        if card=="Ace":
            if tot>=11:
                val=1
            else:
                val=11
            name="Ace"
    return val,name

def extractrandom(tot):
    suit=random.choice(list(cards.keys()))
    card=random.choice(cards[suit])
    cards[suit].remove(card)
    val=0
    name=""
    val,name=extractval(card,tot)
    return val,name,suit

while True:
    print("\n")
    # initial player card
    sumP=0
    sumC=0
    p=[]
    c=[]
    for i in range(0,2):
        valP,nameP,suitP=extractrandom(sumP)
        print(f"player card: {nameP} of {suitP}")
        p.append(valP)
        sumP+=valP
    print(f"player card values: {p}")
    print("\n")
    # initial comp card
    valC,nameC,suitC=extractrandom(sumC)
    print(f"comp card: {nameC} of {suitC}")
    c.append(valC)
    print(f"comp card values: {c}")
    print("\n")
    sumC+=valC
    valC,nameC,suitC=extractrandom(sumC)
    c.append(valC)
    sumC+=valC

    while (sumP<=21 and sumC<=21):
        print("\n")
        #for player
        choice = input("Hit or Stand? (h/s): ")
        print("\n")
        if choice == "h":
            valP,nameP,suitP = extractrandom(sumP)
            print(f"player card: {nameP} of {suitP}")
            sumP += valP
            p.append(valP)
            print(f"player card values: {p}")

        elif choice == "s":
            while sumC < 19:
                valC,nameC,suitC = extractrandom(sumC)
                c.append(valC)
                sumC += valC
            break

        if sumP==21:
            print(f"player card values: {p}")
            print(f"comp card values: {c}")
            print("Player is the winner with a blackjack")
            break
        print("\n")
        #for comp
        valC,nameC,suitC=extractrandom(sumC)
        c.append(valC)
        print(f"Comp card: __?__ of __?__")
        sumC+=valC
        if sumC==21:
            print(f"player card values: {p}")
            print(f"comp card values: {c}")
            print("Computer is the winner with a blackjack")
            break
    
    print("\n")
    print("=================================================================================")
    print(f"player card values: {p}")
    print(f"comp card values: {c}")
    print("\n")
    print(f"Player sum = {sumP}")
    print(f"Computer sum = {sumC}")
    print("=================================================================================")
    print("\n")

    if sumP > 21:
        print(f"Player exceeded 21 with a sum of {sumP}")
        print(f"Computer finished with a sum of {sumC}")
        print("\n")
        print("Computer is the winner!")

    elif sumC > 21:
        print(f"Computer exceeded 21 with a sum of {sumC}")
        print(f"Player finished with a sum of {sumP}")
        print("\n")
        print("Player is the winner!")

    elif sumP == 21 and sumC != 21:
        print(f"Player hit Blackjack with a sum of {sumP}")
        print(f"Computer finished with a sum of {sumC}")
        print("\n")
        print("Player is the winner with a Blackjack!")

    elif sumC == 21 and sumP != 21:
        print(f"Computer hit Blackjack with a sum of {sumC}")
        print(f"Player finished with a sum of {sumP}")
        print("\n")
        print("Computer is the winner with a Blackjack!")

    elif sumP > sumC:
        print(f"Player finished with a sum of {sumP}")
        print(f"Computer finished with a sum of {sumC}")
        print("\n")
        print(f"Player is the winner by {sumP - sumC} points!")

    elif sumC > sumP:
        print(f"Computer finished with a sum of {sumC}")
        print(f"Player finished with a sum of {sumP}")
        print("\n")
        print(f"Computer is the winner by {sumC - sumP} points!")

    else:
        print(f"Player finished with a sum of {sumP}")
        print(f"Computer finished with a sum of {sumC}")
        print("\n")
        print("The game ends in a tie!")
    print("=================================================================================")
    print("\n")

    ch=input("Wanna go again?(y/n): ")
    if ch=="n":
        break



