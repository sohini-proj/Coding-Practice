import random

cards={
    "spades":["A",2,3,4,5,6,7,8,9,10,"j","k","q"],
    "diamonds":["A",2,3,4,5,6,7,8,9,10,"j","k","q"],
    "hearts":["A",2,3,4,5,6,7,8,9,10,"j","k","q"],
    "clubs":["A",2,3,4,5,6,7,8,9,10,"j","k","q"]
}

suit=random.choice(list(cards.keys()))
print(suit)

card=random.choice(cards[suit])
print(f"{card} of {suit}")

if card.isnumeric():
    print(1)
else:
    print(0)