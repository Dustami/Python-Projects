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
percent_list = {
    '+': lambda a, b: a + (a * b / 100),
    '-': lambda a, b: a - (a * b / 100),
    '*': lambda a, b: a * (b / 100),
    '/': lambda a, b: a / (b / 100) if b != 0 else 'You can`t divide by 0!',
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
deleter = 2
size = 10
answer = 0
#Start
print('Welcome to Terminal Calculator!\nDon`t know commands? Try to print \'help\'!')
while True:
    try:
        enter = input('> ').lower()
        enter = enter.replace('pi', str(math.pi))
        enter = enter.replace('e', str(math.e))
        enter = enter.replace('ans', str(answer))
        result = None
#Operations
    #Program Commands
        commands_match = re.match(r'^\s*(round)\s*(\d+)\s*$', enter)
        if commands_match:
            #Used for commands with numbers
            command = commands_match.group(1)
            command_num = int(commands_match.group(2))
            if command == 'round':
                rounder = command_num
            elif command == 'deleter':
                if command_num%2 == 0:
                    deleter = command_num
            elif command == 'size':
                if command_num%2 == 0:
                    size = command_num
        elif enter == 'help':
            print('To use calculator print what you want (Example: 1+1; 1-1; etc)\nYou can also print \'list\' for more details!')
        elif enter == 'list':
            print('''Here list of all commands and operations!:
(X means your number)
___PROGRAM COMMANDS___
help — used for fast tutorial
list — list of all commands
exit — stoping program
history — you can watch history of actions
history del — deleting your history
round X — configure of how much numbers should be after .
deleter X — configure how much actions should be auto-deleted when reach maximum size of history
size X — configure maximum size of history
___X VARIANTS___
That can be used to make accurate operations
pi — 3.14...
e — 2.718...
ans — your last result
___BASIC OPERATIONS___
X+X — addition
X-X — subraction
X*X — multiplication
X/X — division
___ADVENCED OPERATIONS___
X^X — degree
sqrtX — square root
X+X% — business percentage (10 + 100% = 20)
X-X% — business percentage (10 - 100% = 0)
X*X% — mathematics percentage (10 * 100 = 10)
X/X% — mathematics percentage (10 / 100 = 10)
___CONVERTOR___
X cm to in — converting centimeters into inches
X in to cm — converting inches into centimeters
X m to ft — converting meters into feets
X ft to m — converting feets into meters
X km to mi — converting kilometers into miles
X mi to km — converting miles into kilometers
X C to F — converting Celsius into Fahrenheits
X F to C — converting Fahrenheits into Celsius
___TRIGONOMETRY___
sin X deg — sine of x using degrees
cos X deg — cosine of x using degrees
tan X deg — tangent of x using degrees
asin X deg — arc sine of x using degrees
acos X deg — arc cosine of x using degrees
atan X deg — arc tangent of x using degrees
sin X rad — sine of x using radians
cos X rad — cosine of x using radians
tan X rad — tangent of x using radians
asin X rad — arc sine of x using radians
acos X rad — arc cosine of x using radians
atan X rad — arc tangent of x using radians
___LOGARITHMS___
logX_X — logarithm with your base and your argument
log_X — logarithm with base 10
ln_X — logarithm with base e (2.718...)
lg_x — logarithm with base 2
''')
        elif enter == 'exit':
            break
        elif enter == 'history':
            with open('History.txt', 'r', encoding='utf-8') as file:
                print(f'___HISTORY___\n{file.read().strip()}')
        elif enter == 'history del':
            with open('History.txt', 'w', encoding='utf-8') as file:
                pass
    #Search
        basic_match = re.match(r'^\s*(\d+\.?\d*)\s*([-+*/^])\s*(\d+\.?\d*)\s*$', enter)
        sqrt_match = re.match(r'^\s*(sqrt)\s*(\d+\.?\d*)\s*$', enter)
        percent_match = re.match(r'^\s*(\d+\.?\d*)\s*([-+*/^])\s*(\d+\.?\d*)\s*(%)\s*$', enter)
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
            total = float(percent_match.group(1))
            operator = percent_match.group(2)
            percent = float(percent_match.group(3))
            result = round(percent_list[operator](total, percent), rounder)
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
            answer = str(result)
            result = str(f'= {result}')
            print(result)
            with open('History.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
            if len(lines) >= size:
                lines = lines[deleter:]
                with open('History.txt', 'w', encoding='utf-8') as file:
                    file.writelines(lines)
            with open('History.txt', 'a', encoding='utf-8') as file:
                file.write(f'|> {enter}\n|{result}\n')
    except ValueError:
        print('Value Error!')
