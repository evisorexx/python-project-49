#!/usr/bin/env python3

import sys
sys.path.insert(1, 'brain_games')  # Adding directory brain_games/ to PYTHONPATH

from cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
