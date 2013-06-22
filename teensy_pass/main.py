#!/usr/bin/env python3
"""
Command line interface for Teensy Cli
"""

import argparse
from sys import argv
from os import environ, getcwd

DESCR = """
Teensy Password
by: Marcell Vazquez-Chanlatte, William Kennington III
"""
EPILOG = """ """

COMMANDS = {'ls', 'insert', 'rm', 'edit', 'generate', 'show'}
HELP = {
    'cmd': ', '.join(COMMANDS),
    'key': ''
}

TEENSY_MODULE = 'teensy_pass'

try:
    HOME = environ['PASS_HOME']
except KeyError:
    HOME = getcwd()
try:
    KEY = environ['PASS_KEY']
except KeyError:
    KEY = None

PARSER = argparse.ArgumentParser(description=DESCR, epilog=EPILOG,
                                 add_help=False)
PARSER.add_argument('cmd', nargs=1, default='ls', help=HELP['cmd'])
PARSER.add_argument('-k', '--key', default=KEY, required=KEY is None,
                    help=HELP['key'])


def main():
    """Starts the Teensy CLI"""
    if len(argv) < 2 or argv[1] not in COMMANDS:
        PARSER.print_help()
    else:
        cmd_name = '{0}.{1}'.format(TEENSY_MODULE, argv[1])
        cmd = getattr(__import__(cmd_name, fromlist=[cmd_name]), 'run')
        print(cmd([PARSER]))
