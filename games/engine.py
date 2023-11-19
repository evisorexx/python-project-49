
import sys
import re
import random
import operator
from games.cli import welcome_user


def greeter():
    print('Welcome to the Brain Games!')
    global name
    name = re.findall(r'\w+', welcome_user())[1]
    print(f'Hello, {name}')


# For Even
def even(answer, num, counter):
    match answer:
        case 'yes':
            if num % 2 == 0:
                print('Correct!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'")
                print(f"Let's try again, {name}!")
                sys.exit()
        case 'no':
            if num % 2 != 0:
                print('Correct!')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'")
                print(f"Let's try again, {name}!")
                sys.exit()
        case _:
            if num % 2 == 0:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'yes'")
                print(f"Let's try again, {name}!")
                sys.exit()
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
                print(f"Let's try again, {name}!")
                sys.exit()

    if counter == 2:
        print(f'Congratulations, {name}!')


# For Calculator
def calc(answer, num1, num2, operation, counter):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, }
    try:
        answer = int(answer)
    except ValueError:
        print(f"Result must be an integer!\nLet's try again, {name}")
        sys.exit()
    if int(answer) == ops[operation](max(num1, num2), min(num1, num2)):
        print('Correct!')
    else:
        print(f"{int(answer)} is wrong answer ;(. "
              f"Correct answer was "
              f"{ops[operation](max(num1, num2), min(num1, num2))}")
        print(f"Let's try again, {name}!")
        sys.exit()
    if counter == 2:
        print(f'Congratulations, {name}!')


# For Greatest Common Divisor
def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


def divisions(answer, num1, num2, counter):
    try:
        answer = int(answer)
    except ValueError:
        print(f"Result must be an integer!\nLet's try again, {name}")
        sys.exit()
    check = euclid(num1, num2)
    if int(answer) == check:
        print('Correct!')
    else:
        print(f"{int(answer)} is wrong answer ;(. "
              f"Correct answer was {check}.")
        print(f"Let's try again, {name}!")
        sys.exit()
    if counter == 2:
        print(f'Congratulations, {name}!')


# For Progression
def generation_of_values():
    global prog_list, missing_elem
    prog_list, prog_start = [], random.randint(1, 10)
    step = random.randint(1, 5)
    for i in range(10):
        prog_list.append(prog_start)
        prog_start += step
    prog_str = ' '.join([str(num) for num in prog_list])
    missing_elem = prog_list[random.randint(0, len(prog_list) - 1)]
    return prog_str.replace(str(missing_elem), '..', 1)


def progression(answer, counter):
    try:
        answer = int(answer)
    except ValueError:
        print("Progression element must be an integer!")
        print(f"Let's try again, {name}!")
        sys.exit()
    if answer == missing_elem:
        print('Correct!')
    else:
        print(f"{int(answer)} is wrong answer ;(. "
              f"Correct answer was {missing_elem}.")
        print(f"Let's try again, {name}!")
        sys.exit()
    if counter == 2:
        print(f'Congratulations, {name}!')


# For Prime
def is_prime(answer, num, counter):
    from math import ceil, sqrt
    enum = 2
    match answer:
        case 'yes':
            while enum < ceil(sqrt(num)):
                if num % enum != 0:
                    enum += 1
                    continue
                else:
                    print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                    print(f"Let's try again, {name}!")
                    sys.exit()
            print('Correct!')
        case 'no':
            while enum < ceil(sqrt(num)):
                if num % enum == 0:
                    print('Correct!')
                    break
                elif enum < ceil(sqrt(num)) - 1:
                    enum += 1
                    continue
                else:
                    print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                    print(f"Let's try again, {name}!")
                    sys.exit()
        case _:
            print("You must enter 'yes' or 'no' as answer!")
            print(f"Let's try again, {name}!")
            sys.exit()
    if counter == 2:
        print(f'Congratulations, {name}!')
