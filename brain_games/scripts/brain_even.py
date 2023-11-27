#!/usr/bin/env python3
from brain_games.games.even import is_even
from brain_games.engine import start_game


def main():
    start_game(is_even, 1)


if __name__ == '__main__':
    main()
