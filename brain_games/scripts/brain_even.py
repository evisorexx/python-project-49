#!/usr/bin/env python3

import random
import re
from prompt import string
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = re.findall(r'\w+', welcome_user())[1]
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        num = random.randint(1, 100)
        print('Question: ' + str(num))
        answer = string('Your answer: ')
        match answer:
            case 'yes':
                if num % 2 == 0:
                    print('Correct!')
                else:
                    print("'yes' is wrong answer ;(. Correct answer was 'no'")
                    print(f"Let's try again, {name}")
                    break
            case 'no':
                if num % 2 != 0:
                    print('Correct!')
                else:
                    print("'no' is wrong answer ;(. Correct answer was 'yes'")
                    print(f"Let's try again, {name}")
                    break
            case _:
                if num % 2 == 0:
                    print(f"{answer} is wrong answer ;(. Correct answer was 'yes'")
                    print(f"Let's try again, {name}")
                    break
                else:
                    print(f"{answer} is wrong answer ;(. Correct answer was 'no'")
                    print(f"Let's try again, {name}")
                    break

    if i == 2:
      print(f'Congratulations, {name}')


if __name__ == '__main__':
  main()
