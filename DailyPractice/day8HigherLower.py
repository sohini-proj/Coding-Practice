import random

print("""   
                                              __  ___       __             
                                             / / / (_)___ _/ /_  ___  _____
                                            / /_/ / / __ '/ __ \/ _ \/ ___/
                                           / __  / / /_/ / / / /  __/ /    
                                          /_/ ///_/\__, /_/ /_/\___/_/     
                                            / /  /____/_      _____  _____
                                           / /   / __ \ | /| / / _ \/ ___/
                                          / /___/ /_/ / |/ |/ /  __/ /    
                                         /_____/\____/|__/|__/\___/_/  

""")
print("ONE GAME = 10 CHANCES\n")

search_data = {

    "Tech & Websites": {
        "YouTube | Video sharing platform": 1500000000,
        "Google | Search engine company": 1300000000,
        "Gmail | Email service by Google": 900000000,
        "ChatGPT | AI chatbot by OpenAI": 700000000,
        "Google Translate | Language translation tool": 580000000,
        "Google Maps | Navigation service": 450000000,
        "Wikipedia | Online encyclopedia": 290000000,
        "Canva | Online design platform": 185000000,
        "ChatGPT Login | OpenAI login searches": 180000000,
        "OpenAI | Artificial intelligence company": 135000000,
        "Yahoo | Web portal and search engine": 110000000,
        "Google Docs | Cloud document editor": 100000000
    },

    "Social Media": {
        "Facebook | Social media platform": 950000000,
        "WhatsApp | Messaging application": 850000000,
        "Instagram | Photo and video social app": 780000000,
        "TikTok | Short video social platform": 520000000,
        "Twitter/X | Social media platform": 430000000,
        "Reddit | Discussion forum website": 350000000,
        "LinkedIn | Professional networking site": 320000000,
        "Telegram | Messaging application": 270000000,
        "Snapchat | Photo messaging app": 210000000,
        "Discord | Communication platform for communities": 190000000,
        "Pinterest | Visual discovery platform": 170000000,
        "Threads | Social media by Meta": 90000000
    },

    "Entertainment": {
        "Netflix | Streaming entertainment service": 620000000,
        "Spotify | Music streaming platform": 480000000,
        "Amazon Prime Video | Streaming service": 165000000,
        "Disney Plus | Streaming service": 155000000,
        "Taylor Swift | Singer-songwriter": 220000000,
        "Drake | Music artist": 95000000,
        "BTS | K-pop music group": 180000000,
        "Marvel | Superhero entertainment franchise": 140000000,
        "Anime | Japanese animated entertainment": 130000000,
        "Harry Potter | Fantasy movie franchise": 120000000,
        "Wednesday | Popular Netflix series": 85000000,
        "Avatar | Movie franchise": 70000000
    },

    "Gaming": {
        "Roblox | Online gaming platform": 410000000,
        "Minecraft | Sandbox video game": 390000000,
        "PUBG | Battle royale video game": 250000000,
        "Free Fire | Mobile battle royale game": 155000000,
        "GTA 6 | Upcoming Rockstar video game": 95000000,
        "Fortnite | Online battle royale game": 220000000,
        "Valorant | Competitive FPS game": 180000000,
        "Call of Duty | Shooter video game franchise": 175000000,
        "League of Legends | Multiplayer online battle arena game": 160000000,
        "Steam | PC game distribution platform": 150000000,
        "PlayStation | Gaming console brand": 145000000,
        "Xbox | Gaming console brand": 120000000
    },

    "Sports": {
        "Cricket | International sport": 370000000,
        "IPL | Indian Premier League cricket tournament": 360000000,
        "Cristiano Ronaldo | Football athlete": 210000000,
        "Lionel Messi | Football athlete": 205000000,
        "World Cup | International sports tournament": 150000000,
        "Olympics | International sports event": 115000000,
        "Virat Kohli | Cricket athlete": 100000000,
        "NBA | Professional basketball league": 170000000,
        "Formula 1 | International motorsport championship": 160000000,
        "WWE | Wrestling entertainment company": 140000000,
        "Roger Federer | Tennis athlete": 90000000,
        "Real Madrid | Football club": 95000000
    },

    "Technology": {
        "AI | Artificial intelligence topic": 300000000,
        "AI Tools | Artificial intelligence software tools": 195000000,
        "Coding | Programming related searches": 130000000,
        "Python | Programming language": 125000000,
        "Java | Programming language": 120000000,
        "Adobe Photoshop | Photo editing software": 105000000,
        "Machine Learning | AI subfield": 95000000,
        "Data Science | Analytics and programming field": 85000000,
        "VS Code | Code editor by Microsoft": 80000000,
        "GitHub | Code hosting platform": 78000000,
        "JavaScript | Programming language": 76000000,
        "React | JavaScript frontend library": 65000000
    },

    "Shopping & Brands": {
        "Amazon | E-commerce marketplace": 800000000,
        "iPhone | Apple smartphone product": 175000000,
        "Samsung | Electronics company": 170000000,
        "Apple | Consumer electronics company": 280000000,
        "Nike | Sportswear brand": 210000000,
        "Adidas | Sportswear company": 150000000,
        "Flipkart | Indian e-commerce company": 145000000,
        "Zara | Fashion brand": 80000000,
        "Louis Vuitton | Luxury fashion brand": 70000000,
        "Tesla | Electric vehicle company": 160000000,
        "BMW | Luxury automobile manufacturer": 95000000,
        "Rolex | Luxury watch brand": 60000000
    },

    "Finance": {
        "Bitcoin | Cryptocurrency": 240000000,
        "Bitcoin Price | Cryptocurrency market value": 160000000,
        "Ethereum | Cryptocurrency platform": 90000000,
        "Stock Market | Financial market searches": 140000000,
        "Sensex | Indian stock market index": 80000000,
        "Nifty 50 | Indian stock market index": 70000000,
        "Gold Price | Commodity market search": 120000000,
        "USD to INR | Currency conversion search": 100000000,
        "Share Market | Stock trading topic": 95000000,
        "Trading | Financial activity": 90000000,
        "Crypto | Digital currency topic": 110000000,
        "PayPal | Online payment platform": 75000000
    },

    "People": {
        "Elon Musk | Business entrepreneur": 230000000,
        "Donald Trump | Political figure": 190000000,
        "MrBeast | YouTube creator": 180000000,
        "Selena Gomez | Singer and actress": 150000000,
        "Bill Gates | Microsoft co-founder": 100000000,
        "Jeff Bezos | Amazon founder": 90000000,
        "Narendra Modi | Prime Minister of India": 120000000,
        "Shah Rukh Khan | Bollywood actor": 130000000,
        "Emma Watson | Actress": 80000000,
        "Zendaya | Actress and singer": 75000000,
        "Albert Einstein | Famous scientist": 70000000,
        "Kim Kardashian | Media personality": 85000000
    },

    "Utilities": {
        "Weather | Forecast and climate searches": 550000000,
        "Calculator | Online calculator searches": 145000000,
        "Google Maps | Mapping service by Google": 140000000,
        "Translate | Online translation searches": 130000000,
        "Speed Test | Internet speed checker": 90000000,
        "QR Code Generator | QR creation tool": 80000000,
        "PDF Converter | File conversion utility": 85000000,
        "Time Calculator | Date and time calculation tool": 50000000,
        "Unit Converter | Measurement conversion tool": 65000000,
        "Dictionary | Word meaning search tool": 70000000,
        "Calendar | Date utility tool": 75000000,
        "Currency Converter | Foreign exchange utility": 95000000
    }

}
def hl(a,b):
    if a>b:
        return "a"
    if a<b:
        return "b"
    if a==b:
        return "Draw"

while True:
    score=0
    i=10
    while (i>0):
        print(f"\n\nYour Current score is: {score}\n\n")
        catA=random.choice(list(search_data.keys()))
        print(f"Category_A: {catA}")
        keyA=random.choice(list(search_data[catA].keys()))
        print(f"Search_A: {keyA}")
        print("""
                 _    __    
                | |  / /____
                | | / / ___/
                | |/ (__  ) 
                |___/____(_)

        """)
        catB=random.choice(list(search_data.keys()))
        print(f"Category_B: {catB}")
        keyB=random.choice(list(search_data[catB].keys()))
        print(f"Search_B: {keyB}")
        print()
        print()

        A=search_data[catA][keyA]
        B=search_data[catB][keyB]
        res=hl(A,B)
        ch=input("Which option has higher google searches? ( 'A' OR 'B' ): ")
        if res=="Draw":
            score+=0.5
            print(f"Both have the same number of searches\n{keyA}: {A} searches\n{keyB}: {B} searches")
        elif res=="a" and ch.lower()=="a":
            score+=1
            print(f"Yes! '{keyA}' has higher number of searches\n{keyA}: {A} searches\n{keyB}: {B} searches")
        elif res=="a" and ch.lower()=="b":
            print(f"Nope, '{keyA}' has higher number of searches\n{keyA}: {A} searches\n{keyB}: {B} searches")
        elif res=="b" and ch.lower()=="b":
            score+=1
            print(f"Yes! '{keyB}' has higher number of searches\n{keyA}: {A} searches\n{keyB}: {B} searches")
        elif res=="b" and ch.lower()=="a":
            print(f"Nope, '{keyB}' has higher number of searches\n{keyA}: {A} searches\n{keyB}: {B} searches")
        else:
            print("INVALID INPUT")
        
        i-=1
    print("""
    +==========================================================================================================+
    |                                           -  GAME  OVERRR -                                              |
    +==========================================================================================================+
          
    """)
    print(f"Final score: {score}")
    print()
    ch=input("Do you wanna go again?(y/n): ")
    if ch=="n":
        break