#!/usr/bin/env python3

import random


def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


def gcd_values():
    num1, num2 = random.randint(1, 100), random.randint(1, 50)
    check = euclid(num1, num2)
    question = f'{num1} {num2}'
    return check, question


def divisions(answer, check):
    if answer == check:
        return (True, 'Correct!')
    else:
        return (False, f"{int(answer)} is wrong answer ;(. "
                f"Correct answer was {check}.")
