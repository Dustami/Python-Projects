#Libraries
import re
import math
import json
#Dictionaries
basic_list = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 'You can`t divide by 0!',
    '^': lambda a, b: a ** b,
    }
convert_list = {
    ('cm', 'in'): lambda a: a / 2.54,
    ('in', 'cm'): lambda a: a * 2.54,
    ('m', 'ft'): lambda a: a * 3.28084,
    ('ft', 'm'): lambda a: a / 3.28084,
    ('km', 'mi'): lambda a: a * 0.621371,
    ('mi', 'km'): lambda a: a / 0.621371,
    ('c', 'f'): lambda a: a * 1.8 + 32,
    ('f', 'c'): lambda a: (a - 32) * 5 / 9,
    }
trigon_list = {
    ('sin', 'deg'): lambda a: math.sin(math.radians(a)),
    ('cos', 'deg'): lambda a: math.cos(math.radians(a)),
    ('tan', 'deg'): lambda a: math.tan(math.radians(a)),
    ('sin', 'rad'): lambda a: math.sin(a),
    ('cos', 'rad'): lambda a: math.cos(a),
    ('tan', 'rad'): lambda a: math.tan(a),
    ('asin', 'deg'): lambda a: math.degrees(math.asin(a)),
    ('acos', 'deg'): lambda a: math.degrees(math.acos(a)),
    ('atan', 'deg'): lambda a: math.degrees(math.atan(a)),
    ('asin', 'rad'): lambda a: math.asin(a),
    ('acos', 'rad'): lambda a: math.acos(a),
    ('atan', 'rad'): lambda a: math.atan(a),
    }
#Initial settings
rounder = 12
#Start
print('Welcome to Terminal Calculator!\nDon`t know commands? Try to print \'help\'!')
while True:
    try:
        result = None
        enter = input('> ').lower()
#Operations
    #Program Commands
        commands_match = re.match(r'^\s*(round)\s*(\d+)\s*$', enter)
        if commands_match:
            #Used for commands with numbers
            command = commands_match.group(1)
            command_num = int(commands_match.group(2))
            if command == 'round':
                rounder = command_num
        elif enter == 'help':
            print('To use calculator print what you want (Example: 1+1; 1-1; etc)\nYou can also print \'list\' for more details!')
        elif enter == 'list':
            print('Here list of all operations (\'x\' means your number)\n___Basic operations___\nx+x (for add)\nx-x (for subtract)\nx*x (for multiply)\nx/x (for divide)\n___Advenced operations___\nx^x (for power)\nsqrtx (for square root)\nx% of x (for finding the % of you number)\n___Convert operations___\nx cm to in (for converting centimeters to inches)\nx in to cm (for converting inches to centimeters)\nx m to ft (for converting meters to feets)\nx ft to m (for converting feet to meters)\nx km to mi (for converting kilometers to miles)\nx mi to km (for converting miles to kilometers)\nx C to F (for converting Celsius to Fahrenheit)\nx F to C (for converting Fahrenheit to Celsius)\n___Trigonometry operations___\nsin/cos/tan x deg/rad (for finding sinus or cosinus or tangens with degreees or radians)')
        elif enter == 'stop' or enter == 'exit':
            break
        elif enter == 'history':
            with open('History.txt', 'r', encoding='utf-8') as file:
                print(file.read().strip())
        elif enter == 'history delete' or enter == 'history clear':
            with open('History.txt', 'w', encoding='utf-8') as file:
                file.write('___HISTORY___\n')
    #Search
        basic_match = re.match(r'^\s*(\d+\.?\d*)\s*([-+*/^])\s*(\d+\.?\d*)\s*$', enter)
        sqrt_match = re.match(r'^\s*(sqrt)\s*(\d+\.?\d*)\s*$', enter)
        percent_match = re.match(r'^\s*(\d+\.?\d*)\s*(%)\s*(of)\s*(\d+\.?\d*)\s*$', enter)
        convert_match = re.match(r'^\s*(\d+\.?\d*)\s*(cm|in|m|ft|km|mi|c|f)\s*(to)\s*(cm|in|m|ft|km|mi|c|f)\s*$', enter)
        trigon_match = re.match(r'^\s*(sin|cos|tan|asin|acos|atan)\s*(\d+\.?\d*)\s*(deg|rad)\s*$', enter)
        log_match = re.match(r'^\s*(log|lg|ln)\s*(\d*)\s*(_)\s*(\d+\.?\d*)\s*$', enter)
    #Operations
        if basic_match:
            num1 = float(basic_match.group(1))
            operator = basic_match.group(2)
            num2 = float(basic_match.group(3))
            result = round(basic_list[operator](num1, num2), rounder)
        elif sqrt_match:
            num = float(sqrt_match.group(2))
            result = round(math.sqrt(num1), rounder)
        elif percent_match:
            percent = float(percent_match.group(1))
            total = float(percent_match.group(4))
            result = round(total * percent / 100, rounder)
        elif convert_match:
            num = float(convert_match.group(1))
            value1 = convert_match.group(2)
            value2 = convert_match.group(4)
            result = round(convert_list[value1, value2](num), rounder)
        elif trigon_match:
            operator = trigon_match.group(1)
            num = float(trigon_match.group(2))
            dORr = trigon_match.group(3)
            result = round(trigon_list[operator, dORr](num), rounder)
        elif log_match:
        #Has been error if you try to log_10 (try to use basic log with base 10)
        #So i decided to make this + its much shorter:
            log = log_match.group(1)
            argument = float(log_match.group(4))
            if log == 'log':
                try:
                    base = float(log_match.group(2))
                    result = round(math.log(argument, base), rounder)
                except ValueError:
                    result = round(math.log10(argument), rounder)
            elif log == 'ln':
                result = round(math.log(argument, math.e), rounder)
            elif log == 'lg':
                result = round(math.log2(argument), rounder)
    #Result print and auto write of history
        if result != None:
            result = str(f'= {result}')
            print(result)
            with open('History.txt', 'a', encoding='utf-8') as file:
                file.write(f'|> {enter}\n|{result}\n')
    except ValueError:
        print('Value Error!')
