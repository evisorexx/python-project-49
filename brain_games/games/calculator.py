#!/usr/bin/env python3
import random


def calc():
    num1, num2 = random.randint(1, 30), random.randint(1, 30)
    operation = random.choice(['*', '-', '+'])
    question = f'{max(num1, num2)} {operation} {min(num1, num2)}'
    real_answer = eval(question)
    return str(real_answer), question
