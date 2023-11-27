#!/usr/bin/env python3
import sys
from prompt import string

ROUNDS = 3
START_ANSWERS = [
    'What is the result of the expression?',
    'Answer "yes" if the number is even, otherwise answer "no".',
    'Find the greatest common divisor of given numbers.',
    'Answer "yes" if given number is prime. Otherwise answer "no".',
    'What number is missing in the progression?'
]


def greet():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(game, flag: int):
    name = greet()
    print(START_ANSWERS[flag])
    engine(game, name)


def engine(game, name):
    for i in range(ROUNDS):
        real_answer, question = game()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')
        if real_answer == user_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {real_answer}.")
            print(f"Let's try again, {name}!")
            sys.exit()
    print(f'Congratulations, {name}!')
