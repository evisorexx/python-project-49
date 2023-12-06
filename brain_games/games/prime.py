#!/usr/bin/env python3
import random
from math import ceil, sqrt

START_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 2:
        return True
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i != 0:
            continue
        else:
            return False
    return True


def prime_value():
    return random.randint(2, 97)  # First 25 primes included


def game_output():
    question = prime_value()
    if is_prime(question):
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return real_answer, question
