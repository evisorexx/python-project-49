#!/usr/bin/env python3
import random

START_ANSWER = 'What number is missing in the progression?'


def prog_values():
    prog_list, prog_start = [], random.randint(1, 10)
    step = random.randint(1, 5)
    for i in range(10):
        prog_list.append(prog_start)
        prog_start += step
    prog_str = ' '.join([str(num) for num in prog_list])
    return prog_list, prog_str


def game_output():
    prog_list, prog_str = prog_values()
    real_answer = prog_list[random.randint(0, len(prog_list) - 1)]
    question = prog_str.replace(str(real_answer), '..', 1)
    return str(real_answer), question
