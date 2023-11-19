#!/usr/bin/env python3

import random
from prompt import string
from games.engine import is_prime, greeter


def main():
    greeter()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        num = random.randint(1, 97)  # First 25 primes included
        print(f'Question: {num}')
        answer = string('Your answer: ')
        is_prime(answer, num, i)


if __name__ == '__main__':
    main()
