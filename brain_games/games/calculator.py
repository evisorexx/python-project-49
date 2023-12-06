#!/usr/bin/env python3
import random

START_ANSWER = 'What is the result of the expression?'


def calc_values():
    num1, num2 = random.randint(1, 30), random.randint(1, 30)
    operation = random.choice(['*', '-', '+'])
    return num1, num2, operation


def game_output():
    num1, num2, operation = calc_values()
    question = f'{max(num1, num2)} {operation} {min(num1, num2)}'
    real_answer = str(eval(question))
    return real_answer, question
