#!/usr/bin/env python3
import sys; sys.path.insert(1, 'games')
from prompt import string
from games.calculator import calc, calc_values
from games.even import is_even, even_value
from games.divisor import divisions, gcd_values
from games.prime import is_prime, prime_value
from games.progression import progression, progression_values

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


def which_game(game: str, flag: int):
    name = greet()
    print(START_ANSWERS[flag])
    engine(game, name)


def engine(game, name):
    match game:
        case 'calc':
            for i in range(ROUNDS):
                question = calc_values()[3]
                print(f'Question: {question}')
                answer = string('Your answer: ')
                try:
                    answer = int(answer)
                except ValueError:
                    print(f"Result must be an integer! "
                          f"Let's try again, {name}")
                    sys.exit()
                if calc(question, answer)[0]:
                    print(calc(question, answer)[1])
                else:
                    print(calc(question, answer)[1])
                    print(f"Let's try again, {name}!")
                    sys.exit()
            print(f'Congratulations, {name}!')
        case 'even':
            for i in range(ROUNDS):
                question = even_value()
                print('Question: ' + question)
                answer = string('Your answer: ')
                if is_even(answer, eval(question))[0]:
                    print(is_even(answer, eval(question))[1])
                else:
                    print(is_even(answer, eval(question))[1])
                    print(f"Let's try again, {name}!")
                    sys.exit()
            print(f'Congratulations, {name}!')
        case 'gcd':
            for i in range(ROUNDS):
                check, question = gcd_values()
                print('Question: ' + question)
                answer = string('Your answer: ')
                try:
                    answer = int(answer)
                except ValueError:
                    print(f"Result must be an integer! "
                          f"Let's try again, {name}")
                    sys.exit()
                if divisions(answer, check)[0]:
                    print(divisions(answer, check)[1])
                else:
                    print(divisions(answer, check)[1])
                    print(f"Let's try again, {name}!")
                    sys.exit()
            print(f'Congratulations, {name}!')
        case 'prime':
            for i in range(ROUNDS):
                question = prime_value()
                print('Question: ' + str(question))
                answer = string('Your answer: ')
                if is_prime(answer, question)[0]:
                    print(is_prime(answer, question)[1])
                else:
                    print(is_prime(answer, question)[1])
                    print(f"Let's try again, {name}!")
                    sys.exit()
            print(f'Congratulations, {name}!')
        case 'progression':
            for i in range(ROUNDS):
                question, missing_elem = progression_values()
                print('Question: ' + question)
                answer = string('Your answer: ')
                try:
                    answer = int(answer)
                except ValueError:
                    print("Progression element must be an integer!")
                    print(f"Let's try again, {name}!")
                    sys.exit()
                if progression(answer, missing_elem)[0]:
                    print(progression(answer, missing_elem)[1])
                else:
                    print(progression(answer, missing_elem)[1])
                    print(f"Let's try again, {name}!")
                    sys.exit()
            print(f'Congratulations, {name}!')
