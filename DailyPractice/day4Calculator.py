print(
'''
        ________________________
       |========================|               ___       _____       ___
       |========================|              |___| \  /   |  |   | |   | |\  |
       |------------------------|              |      \/    |  |---| |   | | \ |
       | | 1 | | 2 | | 3 | |AC| |              |      ||    |  |   | |___| |  \|
       | | 4 | | 5 | | 6 | | +| |     ___              ___                 _____  ___   ___
       | | 7 | | 8 | | 9 | | -| |    |      /\   |    |    |   | |      /\   |   |   | |___|
       | |00 | | 0 | | . | | X| |    |     /==\  |    |    |   | |     /==\  |   |   | |\\
       | |tan| |sin| |cos| | /| |    |___ /    \ |___ |___ |___| |___ /    \ |   |___| | \\
       |________________________|
'''
)
def add(a,b):
    return a+b
def sub(a,b):
  return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
    print("\n")
    print("OPERATIONS :\n1. ADD (+)\n2. SUBTRACT (-)\n3. MULTIPLY (*)\n4. Divide (/)")
    print("\n")
    a=float(input("Enter Number 1: "))
    print("\n")
    b=float(input("Enter Number 2: "))
    print("\n")
    op=input("Enter operation( +, -, * or /): ")
    if op=="+":
        print(a,op,b,"=",add(a,b),sep=" ")
    elif op=="-":
        print(a,op,b,"=",sub(a,b),sep=" ")
    elif op=="*":
        print(a,op,b,"=",mult(a,b),sep=" ")
    elif op=="/":
        print(a,op,b,"=",div(a,b),sep=" ")
    else:
        print("INVALID INPUT")
    print("\n")
    ch=input("Wanna go again?(y/n): ")
    if ch=="n":
        break
    