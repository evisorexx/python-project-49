#!/usr/bin/env python3

from prompt import string


def welcome_user():
    name = string('May I have your name? ')
    return f'Hello, {name}!'
