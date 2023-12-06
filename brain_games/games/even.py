#!/usr/bin/env python3
import random

START_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def even_value():
    return random.randint(1, 100)


def game_output():
    question = even_value()
    if is_even(question):
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return real_answer, question
