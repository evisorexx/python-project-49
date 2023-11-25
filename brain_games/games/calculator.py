#!/usr/bin/env python3

import operator
import random

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, }


def calc_values():
    num1, num2 = random.randint(1, 30), random.randint(1, 30)
    operation = random.choice(['*', '-', '+'])
    question = f'{max(num1, num2)} {operation} {min(num1, num2)}'
    return num1, num2, operation, question


def calc(question, answer=None):
    if int(answer) == eval(question):
        return (True, 'Correct!')
    else:
        return (False, (f"{int(answer)} is wrong answer ;(. "
                f"Correct answer was {eval(question)}"))
