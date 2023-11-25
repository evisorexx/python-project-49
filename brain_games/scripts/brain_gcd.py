#!/usr/bin/env python3

import sys
sys.path.insert(1, 'brain_games')  # Adding directory brain_games/ to PYTHONPATH

from engine import which_game


def main():
    which_game('gcd', 2)
    

if __name__ == '__main__':
    main()
