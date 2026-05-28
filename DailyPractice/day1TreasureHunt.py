#this is a treasure hunt game
import random
names=["Dungeon Dragon","Spy Palace Maid","Knight Wolf","Mystic Merchant"]
boat=["You wait patiently along the shore, but no boat ever arrives. As the sun sets and darkness takes over, your journey comes to an unfortunate end.","A lonely boat emerges through the thick fog and offers you passage to the island. But midway through the journey, you discover the horrifying truth — the boat is carrying survivors infected from a zombie apocalypse. Within moments, chaos erupts, and you meet a grim fate in the middle of the sea.","After a long and dangerous journey across the waters, you finally reach the mysterious island. Hidden deep within ancient ruins, you uncover the legendary treasure you had been searching for. Victory is yours."]
swim=["You dive into the cold waters and begin swimming toward the island. Suddenly, a massive shark emerges from the depths and attacks without warning. Your adventure ends beneath the waves.","Halfway through the journey, dark clouds gather overhead and a violent storm erupts across the sea. The raging currents pull you into the endless abyss, and you are never seen again.","Fighting against the powerful waves, you push forward with determination and finally reach the island. But Alas! you are too exhausted to carry on"]
night=["Under the cover of darkness, you quietly slip through the castle gates. But before you can take another step, the Royal Sorcerer senses your presence. With a single bolt of lightning, he strikes you down instantly.","As you wander through the silent halls of the castle, a restless ghost begins to follow you. The spirit lures you deep into the royal treasury, where the doors suddenly seal shut behind you. Trapped forever among endless gold and cursed relics, your fate is sealed.","You successfully sneak into the castle and make your way through the ancient corridors. But hidden within the shadows is the castle's darkest secret — the prince is a terrifying werewolf. The beast lunges at you without warning, and your adventure comes to a brutal end."]
climb=["You begin climbing the steep cliff beneath the blazing sun. As the heat grows unbearable, your vision starts to blur and strange whispers echo in your mind. Suddenly, startled by the sight of a terrifying wild beast, you lose your grip and fall into the rocks below. Whether it was real or merely a trick of your mind... or the work of the Royal Sorcerer... remains a mystery.","Determined to reach the castle quickly, you secure your rope and continue the dangerous climb. But halfway up the cliff, your worn-out equipment gives way. The rope snaps without warning, sending you plunging into the abyss below.","After an exhausting climb, you finally reach the top of the cliff and step into the castle grounds. But the guards were expecting intruders. Surrounded from every direction with no chance of escape, you are captured and thrown into the castle dungeon, never to be seen again."]
while True:
    print("\n")
    print("!!! WELCOME TO PYTHON TREASURE HUNT CHALLENGE !!!")
    print("~~~~~~~~ CAN YOU ACCOMPLISH THE MISSION? ~~~~~~~~")
    print("\n")
    mn=random.choice(names)
    print("A legendary treasure has been hidden somewhere in this mysterious land of Eledoria, and it’s up to you to find it.\nExplore different paths, make the right choices, and overcome the obstacles standing in your way.\n\nBe careful — one wrong move could end your adventure.\n\nYour goal is simple:\nFind the hidden treasure.")
    print("\n")
    print("Your official mission name is "+mn)
    print("MAY VICTORY BE YOURS!")
    print("\n")

    ch1=input(mn+", you find yourself stranded at a crossroad.\nWhere will you go?(left/right)")
    print("\n")
    if ch1=="left":
        print("ALL ROADS LEAD TO ROME\nGood for you, you've shosen the shortest path")
    if ch1=="right":
        print("ALL ROADS LEAD TO ROME\nJust HOW did you manage to choose the LONGEST!\n"+mn+", you must make better decisions!")
    print("\n")

    ch2=input("As you stand at the edge of the shoreline, two paths lie before you.\nFar across the horizon, a mysterious island rises from the sea, wrapped in fog and secrets untold. To your right, high above the crashing waves, stands an ancient castle perched on the edge of a towering cliff.\nBoth places may hold clues to the hidden treasure...\nWhere would you like to go?(island/castle): ")
    print("\n")
    if ch2=="island":
        print("\n")
        op=input("You arrive at the edge of the water, staring toward the distant island. The waves crash against the shore as the wind howls around you.\n\nThere are two ways to reach the island:\n1. Wait for a passing boat\n2. Swim across the sea\nWhat will you choose?(1/2): ")
        if op=="1":
            res=random.choice(boat)
            print(res)
        if op=="2":
            res=random.choice(swim)
            print(res)

    if ch2=="castle":
        op=input("You make your way toward the towering castle standing high above the cliffs. Its ancient walls loom over the sea, silent and intimidating, as if guarding secrets long forgotten.\nThe path ahead is dangerous, and you must decide how to enter.\n1. Wait until nightfall and sneak into the castle under the cover of darkness\n2. Waste no time and climb the cliff during daylight\nChoose your approach carefully.(1/2): ")
        if op=="1":
            res=random.choice(night)
            print(res)
        if op=="2":
            res=random.choice(climb)
            print(res)
    print("\n")
    print("\n")
    cont=input("Perhaps another try shall get you closer to victory\nFancy goung again?(y/n): ")
    if cont=="n":
        break