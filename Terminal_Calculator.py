import math
def get_num(type="Num: "):
    num = float(input(type))
    return(num)
print("Welcome to Terminal Calculator!\nNeed help? Print help for list of basic commands.")
while True:
    try:
        command = input().lower()
        if command == "help":
            print("Program commands: help, list, stop;\nBasic commands: add, subtract, multiply, divide, power, square root, percentage;\nNeed more commands? Try to print list!")
        elif command == "list":
            print("There list of all commands:\nProgram commands: help, list, stop\nBasic: add subtract, multiply, divide, power, square root, percentage OR +, -, *, /, ^, sqrt, %\nConvert commands: convert, temp, length\n")
        elif command == "stop":
            break
#basics commands
        elif command == "add" or command == "+":
            print(get_num() + get_num())
        elif command == "subtract" or command == "-":
            print(get_num() - get_num())
        elif command == "multiply" or command == "*":
            print(get_num() * get_num())
        elif command == "divide" or command == "/":
            num1_divide = get_num()
            num2_divide = get_num()
            if not num2_divide == 0:
                print(num1_divide / num2_divide)
            else:
                print("You can`t divide by 0!")
        elif command == "power" or command == "^":
            print(get_num() ** get_num())
        elif command == "square root" or command == "sqrt":
            print(math.sqrt(get_num()))
        elif command == "percentage" or command == "%":
            percent_question = input("What you want to find?\npart, total or percentage?\n").lower()
            if percent_question == "part":
                print(get_num("Total num: ") * get_num("Percentage: ") / 100)
            elif percent_question == "total":
                print(get_num("Part: ") * 100 / get_num("Percentage: "))
            elif percent_question == "percentage":
                print(get_num("Part: ") * 100 / get_num("Total num: "))
            else:
                print("Try to print part, total or percentage!")
#converter
        elif command == "convert":
            unit = input("What unit you want convert? (temp or length): ").lower()
            if unit == "temp":
                temp = input("Celsius to Fahrenheit or Fahrenheit to Celsius? (C or F): ").upper()
                if temp == "C":
                    print(f"{get_num("Celsius: ") * 1.8 + 32} ℉")
                elif temp == "F":
                    print(f"{(get_num("Fahrenheit: ") - 32) * 5 / 9} ℃")
                else:
                    print("Try to print C or F!")
            elif unit == "length":
                length = input("Centimeters to Inches or Inches to Centimeters? Meters to Feet or Feet to Meters? Kilometers to Miles or Miles to Kilometers? (cm or in, m or ft, km or mi): ").lower()
                if length == "cm":
                    print(f"{get_num("Centimeters: ") / 2.54} in")
                elif length == "in":
                    print(f"{get_num("Inches: ") * 2.54} cm")
                elif length == "m":
                    print(f"{get_num("Meters: ") * 3.28084} ft")
                elif length == "ft":
                    print(f"{get_num("Feet: ") / 3.28084} m")
                elif length == "km":
                    print(f"{get_num("Kilometers: ") * 0.621371} mi")
                elif length == "mi":
                    print(f"{get_num("Miles: ") / 0.621371} km")
                else:
                    print("Try to print cm or in, m or ft, km or mi!")
            else:
                print("Try to print temp or length!")
        else:
            print("Don`t know commands? Try to print help!")
    except ValueError:
        print("Value error!")
