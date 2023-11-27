#!/usr/bin/env python3
import random
from math import ceil, sqrt


def is_prime():
    question = random.randint(2, 97)  # First 25 primes included
    if question == 2:
        real_answer = 'yes'
        return real_answer, question
    for i in range(2, ceil(sqrt(question)) + 1):
        if question % i != 0:
            continue
        else:
            real_answer = 'no'
            return real_answer, question
    real_answer = 'yes'
    return real_answer, question
