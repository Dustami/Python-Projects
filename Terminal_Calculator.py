import math
while True:
    command = input()
    if command == "help":
        print("Here basics commands for calculator, if you want to view full list of commands print \"list\"\nProgram commands: help, list, break\nBasic commands: add, subtract, multiply, divide OR +, -, *, /\nAdvenced commands: times, root, percentage OR ^, sqrt, %")
    elif command == "stop":
        break
    elif command == "add" or command == "+":
        print(float(input("Number 1: ")) + float(input("Number 2: ")))
    elif command == "subtract" or command == "-":
        print(float(input("Number 1: ")) - float(input("Number 2: ")))
    elif command == "multiply" or command == "*":
        print(float(input("Number 1: ")) * float(input("Number 2: ")))
    elif command == "divide" or command == "/":
        print(float(input("Number 1: ")) / float(input("Number 2: ")))
    elif command == "times" or command == "^":
        print(float(input("Number 1: ")) ** float(input("Number 2: ")))
    elif command == "root" or command == "sqrt":
        print(math.sqrt(float(input("Number: "))))
    elif command == "percentage" or command == "%":
        while True:
            percentage = input("Find number of 100%, number of x% or % of xnumber? (n100, n%, %n): ")
            if percentage == "n100":
                print(float(input("Number of x%: ")) * 100 / float(input("x%: ")))
                break
            elif percentage == "n%":
                print(float(input("Number of 100%: ")) * float(input("x%: ")) / 100)
                break
            elif percentage == "%n":
                print(float(input("Number of x%: ") * 100 / float(input("Number of 100%: "))))
                break
            else:
                print("Invalid answer")
    else:
        print("Command didn`t exist")
