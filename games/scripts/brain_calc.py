#!/usr/bin/env python3

import random
from prompt import string
from games.engine import calc, greeter


def main():
    greeter()
    print('What is the result of the expression?')
    for i in range(3):
        num1, num2 = random.randint(1, 30), random.randint(1, 30)
        operation = random.choice(['*', '-', '+'])
        print(f'Question: {max(num1, num2)} {operation} {min(num1, num2)}')
        answer = string('Your answer: ')
        calc(answer, num1, num2, operation, i)


if __name__ == '__main__':
    main()
