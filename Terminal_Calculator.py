#Library
import math
import re
#Basic operations
def calculating(enter):
    find_match = re.match(r'^\s*(\d+\.?\d*)\s*([-+*/^])\s*(\d+\.?\d*)\s*$', enter)
    if find_match:
        num1 = float(find_match.group(1))
        operator = find_match.group(2)
        num2 = float(find_match.group(3))
        oper_list = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y if y != 0 else "You can`t divide by 0!",
            "^": lambda x, y: x ** y,
        }
        return oper_list[operator](num1, num2)
    return "Unknown format!"
while True:
    try:
        enter = input("> ").lower()
#program commands
        if enter == "help":
            print("here help!")
        elif enter == "stop":
            break
#Search for operations
        sqrt_match = re.match(r'^\s*(sqrt)\s*(\d+\.?\d*)\s*$', enter)
        percent_match = re.match(r'^\s*(\d+\.?\d*)\s*(%)\s*(of)\s*(\d+\.?\d*)\s*$', enter)
    #length search
        centimeter_match = re.match(r'^\s*(\d+\.?\d*)\s*(cm)\s*(to)\s*(in)\s*$', enter)
        inch_match = re.match(r'^\s*(\d+\.?\d*)\s*(in)\s*(to)\s*(cm)\s*$', enter)
        meter_match = re.match(r'^\s*(\d+\.?\d*)\s*(m)\s*(to)\s*(ft)\s*$', enter)
        foot_match = re.match(r'^\s*(\d+\.?\d*)\s*(ft)\s*(to)\s*(m)\s*$', enter)
        kilometer_match = re.match(r'^\s*(\d+\.?\d*)\s*(km)\s*(to)\s*(mi)\s*$', enter)
        mile_match = re.match(r'^\s*(\d+\.?\d*)\s*(mi)\s*(to)\s*(km)\s*$', enter)
    #temperature search
        celsius_match = re.match(r'^\s*(\d+\.?\d*)\s*(C)\s*(to)\s*(F)\s*$', enter)
        fahrenheit_match = re.match(r'^\s*(\d+\.?\d*)\s*(F)\s*(to)\s*(C)\s*$', enter)
#Square root
        if sqrt_match:
            num = float(sqrt_match.group(2))
            print(f"= {math.sqrt(num)}")
        elif percent_match:
            percent = float(percent_match.group(1))
            total = float(percent_match.group(4))
            print(f"= {total * percent / 100}")
#Converter zone
    #length converter
        elif centimeter_match:
            centimeter = float(centimeter_match.group(1))
            print(f"= {centimeter / 2.54} in")
        elif inch_match:
            inch = float(inch_match.group(1))
            print(f"= {inch * 2.54} m")
        elif meter_match:
            meter = float(meter_match.group(1))
            print(f"= {meter * 3.28084} ft")
        elif foot_match:
            foot = float(foot_match.group(1))
            print(f"= {foot / 3.28084} m")
        elif kilometer_match:
            kilometer = float(kilometer_match.group(1))
            print(f"= {kilometer * 0.621371} mi")
        elif mile_match:
            mile = float(mile_match.group(1))
            print(f"= {mile / 0.621371} km")
    #temperature converter
        elif celsius_match:
            celsius = float(celsius_match.group(1))
            print(f"= {celsius * 1.8 + 32} ℉")
        elif fahrenheit_match:
            fahrenheit = float(fahrenheit_match.group(1))
            print(f"= {(fahrenheit - 32) * 5 / 9} ℃")
#Basic operations and Error
        else:
            print(f"= {calculating(enter)}")
    except ValueError:
        print("Numbers Error!")
