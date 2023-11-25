#!/usr/bin/env python3

import random


def even_value():
    num = random.randint(1, 100)
    question = str(num)
    return question


def is_even(answer, num):
    match answer:
        case 'yes':
            if num % 2 == 0:
                return (True, 'Correct!')
            else:
                return (False, "'yes' is wrong answer ;(. "
                        "Correct answer was 'no'")
        case 'no':
            if num % 2 != 0:
                return (True, 'Correct!')
            else:
                return (False, "'no' is wrong answer ;(. "
                        "Correct answer was 'yes'")
        case _:
            if num % 2 == 0:
                return (False, f"'{answer}' is wrong answer ;(. "
                        "Correct answer was 'yes'")
            else:
                return (False, f"'{answer}' is wrong answer ;(. "
                        "Correct answer was 'no'")
