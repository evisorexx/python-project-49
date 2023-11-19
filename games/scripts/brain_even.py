#!/usr/bin/env python3

import random
from prompt import string
from games.engine import even, greeter


def main():
    greeter()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        num = random.randint(1, 100)
        print('Question: ' + str(num))
        answer = string('Your answer: ')
        even(answer, num, i)


if __name__ == '__main__':
    main()
