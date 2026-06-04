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
operators={"+":add,"-":sub,"*":mult,"/":div}
while True:
    print("\n")
    print("OPERATIONS :\n1. ADD (+)\n2. SUBTRACT (-)\n3. MULTIPLY (*)\n4. Divide (/)")
    print("\n")
    a=float(input("Enter Number 1: "))
    print("\n")
    b=float(input("Enter Number 2: "))
    print("\n")
    op=input("Enter operation( +, -, * or /): ")
    print("\n")
    if op in operators:
        print(f" {a} {op} {b} = {operators[op](a,b)}")
    print("\n")
    ch=input("Wanna go again?(y/n): ")
    if ch=="n":
        break
    