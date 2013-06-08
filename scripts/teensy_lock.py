#!/usr/bin/env python3
"""
Command line interface for Teensy Cli
"""

import argparse

DESCR = """
Teensy Password
by: Marcell Vazquez-Chanlatte, William Kennington III
"""
EPILOG = """ """


def show(args):
    """ """
    raise NotImplementedError


def ls_pass(args):
    """ """
    raise NotImplementedError


def insert(args):
    """ """
    raise NotImplementedError


def remove(args):
    """ """
    raise NotImplementedError


def edit(args):
    """ """
    raise NotImplementedError


def generate(args):
    """ """
    raise NotImplementedError


COMMANDS = {
    'show': show,
    'ls:': ls_pass,
    'insert': insert,
    'rm': remove,
    'edit': edit,
    'generate': generate,
}

HELP = {
    'cmd': ', '.join(COMMANDS.keys()),
}


def main():
    """Starts the Teensy CLI"""
    parser = argparse.ArgumentParser(description=DESCR, epilog=EPILOG)
    parser.add_argument('cmd', nargs='*', default=['ls'], help=HELP['cmd'])
    args = parser.parse_args()

    COMMANDS[args.cmd[0]](args)

if __name__ == '__main__':
    main()
