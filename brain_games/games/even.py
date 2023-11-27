#!/usr/bin/env python3
import random


def is_even():
    question = random.randint(1, 100)
    if question % 2 == 0:
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return real_answer, question
