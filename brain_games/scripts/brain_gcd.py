#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.engine import start_game


def main():
    start_game(gcd, 2)


if __name__ == '__main__':
    main()
