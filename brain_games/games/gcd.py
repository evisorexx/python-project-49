#!/usr/bin/env python3
import random


def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


def gcd():
    num1, num2 = random.randint(1, 100), random.randint(1, 50)
    real_answer = euclid(num1, num2)
    question = f'{num1} {num2}'
    return str(real_answer), question
