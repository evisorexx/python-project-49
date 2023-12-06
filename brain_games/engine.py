#!/usr/bin/env python3
import sys
from prompt import string

ROUNDS = 3


def greet():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(game):
    name = greet()
    print(game.START_ANSWER)
    for round in range(ROUNDS):
        real_answer, question = game.game_output()
        engine(real_answer, question, name)
    print(f'Congratulations, {name}!')


def engine(real_answer, question, name):
    print(f'Question: {question}')
    user_answer = string('Your answer: ')
    if real_answer == user_answer:
        print('Correct!')
    else:
        print(f"{user_answer} is wrong answer ;(. "
              f"Correct answer was {real_answer}.")
        print(f"Let's try again, {name}!")
        sys.exit()
