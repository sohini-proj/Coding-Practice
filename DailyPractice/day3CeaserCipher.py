alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(s,shift):
    s2=""
    for i in s:
        ind=s.index(i)
        pos=alphabet.index(i)
        newpos=(pos+shift)%26
        let=alphabet[newpos]
        s2+=let
    return s2

def decode(s,shift):
    s2=""
    for i in s:
        ind=s.index(i)
        pos=alphabet.index(i)
        newpos=(pos-shift)%26
        let=alphabet[newpos]
        s2+=let
    return s2

while True:
    print("\n")
    print("------------- PYTHON CEASER CIPHER -------------")
    print("\n")
    print("1. ENCODE\n2. DECODE\n")
    ch=int(input("Do you want to encode or decode(1/2): ").lower())
    print("\n")
    if ch==1:
        s=input("Enter CODE to ENCODE: ")
        print("\n")
        shift=int(input("Enter number of places to shift right: "))
        print("\n")
        print("Your Code is: ",encode(s,shift))
    if ch==2:
        s=input("Enter CODE to DECODE: ")
        print("\n")
        shift=int(input("Enter number of places to shift left: "))
        print("\n")
        print("Your Code is: ",decode(s,shift))
    print("\n")
    op=input("Wanna go again?(y/n): ")
    if op=="n":
        break


