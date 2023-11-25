#!/usr/bin/env python3
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from brain_games.engine import which_game


def main():
    which_game('calc', 0)


if __name__ == '__main__':
    main()
