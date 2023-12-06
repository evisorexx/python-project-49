#!/usr/bin/env python3
import random

START_ANSWER = 'Find the greatest common divisor of given numbers.'


def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


def gcd_values():
    return random.randint(1, 100), random.randint(1, 50)


def game_output():
    num1, num2 = gcd_values()
    real_answer = euclid(num1, num2)
    question = f'{num1} {num2}'
    return str(real_answer), question
