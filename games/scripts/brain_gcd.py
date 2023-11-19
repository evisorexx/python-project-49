#!/usr/bin/env python3

import random
from prompt import string
from games.engine import divisions, greeter


def main():
    greeter()
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        num1, num2 = random.randint(1, 100), random.randint(1, 50)
        print(f'Question: {num1} {num2}')
        answer = string('Your answer: ')
        divisions(answer, num1, num2, i)


if __name__ == '__main__':
    main()
