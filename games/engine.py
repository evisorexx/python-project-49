
import sys
import re
import operator
from games.cli import welcome_user


def greeter():
    print('Welcome to the Brain Games!')
    global name
    name = re.findall(r'\w+', welcome_user())[1]


def even(answer, num, counter):
    match answer:
        case 'yes':
            if num % 2 == 0:
                print('Correct!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'")
                print(f"Let's try again, {name}")
                sys.exit()
        case 'no':
            if num % 2 != 0:
                print('Correct!')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'")
                print(f"Let's try again, {name}")
                sys.exit()
        case _:
            if num % 2 == 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
                print(f"Let's try again, {name}")
                sys.exit()
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
                print(f"Let's try again, {name}")
                sys.exit()

    if counter == 2:
        print(f'Congratulations, {name}!')


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
        print(f"{int(answer)} is wrong answer ;(. " \
            f"Correct answer was " \
            f"{ops[operation](max(num1, num2), min(num1, num2))}")
        print(f"Let's try again, {name}")
        sys.exit()
    if counter == 2:
        print(f'Congratulations, {name}!')


def divisions(answer, num1, num2, counter):
    try:
        answer = int(answer)
    except ValueError:
        print(f"Result must be an integer!\nLet's try again, {name}")
        sys.exit()
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    if int(answer) == num2:
        print('Correct!')
    else:
        print(f"{int(answer)} is wrong answer ;(. " \
              f"Correct answer was {num2}.")
        print(f"Let's try again, {name}")
        sys.exit()
    if counter == 2:
        print(f'Congratulations, {name}!')