#!/usr/bin/env python3
"""
Command line interface for Teensy Cli
"""

import argparse

DESCR = """
Teensy Password
by: Marcell Vazquez-Chanlatte, William Kennington III
"""
EPILOG = """or you know you could take this by hand..."""

HELP = {
    'key': 'Key that the password is stored under.',
    'list': 'List all stored password.',
    'pass': 'Return the password.',
    'user': 'Return the username.',
    'set': 'Set all fields specified.',
    'remove': 'Remove specified entry.',
    'generate': 'specify the length of password to generate.'
}

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description=DESCR, epilog=EPILOG)
    PARSER.add_argument('-k', '--key', dest='key', type=str, help=HELP['key'])
    PARSER.add_argument('-l', '--list',  action='store_true', help=HELP['list'])
    PARSER.add_argument('-u', '--user',  action='store_true', help=HELP['user'])
    PARSER.add_argument('-p', '--password', action='store_true',
                        help=HELP['pass'])
    PARSER.add_argument('-s', '--set',  action='store_true', help=HELP['set'])
    PARSER.add_argument('-r', '--remove',  action='store_true')
    PARSER.add_argument('-g', '--generate', type=int, help=HELP['generate'])
    ARGS = PARSER.parse_args()
