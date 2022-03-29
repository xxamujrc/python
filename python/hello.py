intro = input("""
Would you like to greet[1] or Solve problem[2]?
""")


def Sum():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(a+b)


def greet():
    print("Hello World💙")


while 1:
    if intro == "1":
        greet()
        break
    elif intro == "2":
        Sum()
        break
    else:
        print("Error 404")
        break
