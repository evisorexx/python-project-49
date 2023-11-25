#!/usr/bin/env python3

import random


def progression_values():
    prog_list, prog_start = [], random.randint(1, 10)
    step = random.randint(1, 5)
    for i in range(10):
        prog_list.append(prog_start)
        prog_start += step
    prog_str = ' '.join([str(num) for num in prog_list])
    missing_elem = prog_list[random.randint(0, len(prog_list) - 1)]
    res_str = prog_str.replace(str(missing_elem), '..', 1)
    return res_str, missing_elem


def progression(answer, missing_elem):
    if answer == missing_elem:
        return (True, 'Correct!')
    else:
        return (False, f"{int(answer)} is wrong answer ;(. "
              f"Correct answer was {missing_elem}.")
