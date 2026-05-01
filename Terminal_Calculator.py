#Libraries
import re
import math
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
    ('sin', 'deg'): lambda a: round(math.sin(math.radians(a)), 12),
    ('cos', 'deg'): lambda a: round(math.cos(math.radians(a)), 12),
    ('tan', 'deg'): lambda a: round(math.tan(math.radians(a)), 12),
    ('sin', 'rad'): lambda a: round(math.sin(a), 12),
    ('cos', 'rad'): lambda a: round(math.cos(a), 12),
    ('tan', 'rad'): lambda a: round(math.tan(a), 12),
    ('asin', 'deg'): lambda a: round(math.degrees(math.asin(a)), 12),
    ('acos', 'deg'): lambda a: round(math.degrees(math.acos(a)), 12),
    ('atan', 'deg'): lambda a: round(math.degrees(math.atan(a)), 12),
    ('asin', 'rad'): lambda a: round(math.asin(a), 12),
    ('acos', 'rad'): lambda a: round(math.acos(a), 12),
    ('atan', 'rad'): lambda a: round(math.atan(a), 12),
    }
#Start
print('Welcome to Terminal Calculator!\nDon`t know commands? Try to print \'help\'!')
while True:
    try:
        enter = input('> ').lower()
#Operations
    #Program Commands
        if enter == 'help':
            print('To use calculator print what you want (Example: 1+1; 1-1; etc)\nYou can also print \'list\' for more details!')
        elif enter == 'list':
            print('Here list of all operations (\'x\' means your number)\n___Basic operations___\nx+x (for add)\nx-x (for subtract)\nx*x (for multiply)\nx/x (for divide)\n___Advenced operations___\nx^x (for power)\nsqrtx (for square root)\nx% of x (for finding the % of you number)\n___Convert operations___\nx cm to in (for converting centimeters to inches)\nx in to cm (for converting inches to centimeters)\nx m to ft (for converting meters to feets)\nx ft to m (for converting feet to meters)\nx km to mi (for converting kilometers to miles)\nx mi to km (for converting miles to kilometers)\nx C to F (for converting Celsius to Fahrenheit)\nx F to C (for converting Fahrenheit to Celsius)\n___Trigonometry operations___\nsin/cos/tan x deg/rad (for finding sinus or cosinus or tangens with degreees or radians)')
        elif enter == 'stop' or enter == 'exit':
            break
    #Search
        basic_match = re.match(r'^\s*(\d+\.?\d*)\s*([-+*/^])\s*(\d+\.?\d*)\s*$', enter)
        sqrt_match = re.match(r'^\s*(sqrt)\s*(\d+\.?\d*)\s*$', enter)
        percent_match = re.match(r'^\s*(\d+\.?\d*)\s*(%)\s*(of)\s*(\d+\.?\d*)\s*$', enter)
        convert_match = re.match(r'^\s*(\d+\.?\d*)\s*(cm|in|m|ft|km|mi|c|f)\s*(to)\s*(cm|in|m|ft|km|mi|c|f)\s*$', enter)
        trigon_match = re.match(r'^\s*(sin|cos|tan|asin|acos|atan)\s*(\d+\.?\d*)\s*(deg|rad)\s*$', enter)
    #Operations
        if basic_match:
            num1 = float(basic_match.group(1))
            operator = basic_match.group(2)
            num2 = float(basic_match.group(3))
            print(f'= {basic_list[operator](num1, num2)}')
        elif sqrt_match:
            num = float(sqrt_match.group(2))
            print(f'= {math.sqrt(num1)}')
        elif percent_match:
            percent = float(percent_match.group(1))
            total = float(percent_match.group(4))
            print(f'= {total * percent / 100}')
        elif convert_match:
            num = float(convert_match.group(1))
            value1 = convert_match.group(2)
            value2 = convert_match.group(4)
            print(f'= {convert_list[value1, value2](num)}')
        elif trigon_match:
            operator = trigon_match.group(1)
            num = float(trigon_match.group(2))
            dORr = trigon_match.group(3)
            print(f'= {trigon_list[operator, dORr](num)}')
    except ValueError:
        print('Value Error!')
