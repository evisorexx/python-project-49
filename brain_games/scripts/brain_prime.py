#!/usr/bin/env python3
from brain_games.games.prime import is_prime
from brain_games.engine import start_game


def main():
    start_game(is_prime, 3)


if __name__ == '__main__':
    main()
