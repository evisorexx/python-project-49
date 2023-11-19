#!/usr/bin/env python3

from prompt import string
from games.engine import progression, greeter, generation_of_values


def main():
    greeter()
    print('What number is missing in the progression?')
    for i in range(3):
        print(f'Question: {generation_of_values()}')
        answer = string('Your answer: ')
        progression(answer, i)


if __name__ == '__main__':
    main()
