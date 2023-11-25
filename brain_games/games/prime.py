#!/usr/bin/env python3

import random
from math import ceil, sqrt


def prime_value():
    num = random.randint(2, 97)  # First 25 primes included
    return num


def is_prime(answer, num):
    enum = 2
    match answer:
        case 'yes':
            while enum <= ceil(sqrt(num)):
                if num % enum != 0:
                    enum += 1
                    continue
                else:
                    return (False, "'yes' is wrong answer ;(. "
                            "Correct answer was 'no'.")
            return (True, 'Correct!')
        case 'no':
            while enum <= ceil(sqrt(num)):
                if num % enum == 0:
                    return (True, 'Correct!')
                elif enum <= ceil(sqrt(num)) - 1:
                    enum += 1
                    continue
                else:
                    return (False, "'no' is wrong answer ;(. "
                            "Correct answer was 'yes'.")
        case _:
            return (False, "You must enter 'yes' or 'no' as answer!")
