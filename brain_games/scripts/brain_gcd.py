#!/usr/bin/env python3
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from engine import which_game


def main():
    which_game('gcd', 2)


if __name__ == '__main__':
    main()
