#!/usr/bin/env python3
from brain_games.games.progression import progression
from brain_games.engine import start_game


def main():
    start_game(progression, 4)


if __name__ == '__main__':
    main()
