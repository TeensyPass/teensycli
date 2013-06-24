#!/usr/bin/env python3
"""
Command line interface for Teensy Cli
"""

import argparse
from sys import argv
from os import environ, getcwd
from functools import wraps

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
    KEY, NARGS = environ['PASS_KEY'], 2
except KeyError:
    KEY, NARGS = None, 4
    
PARSER = argparse.ArgumentParser(description=DESCR, epilog=EPILOG)
PARSER.add_argument('cmd', nargs='?', default='ls', help=HELP['cmd'])
PARSER.add_argument('-k', '--key', default=KEY, required=KEY is None,
                    help=HELP['key'])


def child_parser(docs):
    """Builds a child parser based on documentation dictionary"""
    def _child_parser(func):
        @wraps(func)
        def __child_parser(parents, argv=argv[1:]):
            parser = argparse.ArgumentParser(parents=parents, add_help=False)
            for opt in docs.keys():
                parser.add_argument('-{0}'.format(opt[0]), '--{0}'.format(opt),
                                    required=True, help=docs[opt])
            return func(parser.parse_args(argv))
        return __child_parser
    return _child_parser


def main():
    """Starts the Teensy CLI"""
    args = PARSER.parse_args(argv[1:NARGS])
    cmd_name = '{0}.{1}'.format(TEENSY_MODULE, args.cmd)
    cmd = getattr(__import__(cmd_name, fromlist=[cmd_name]), 'run')
    print(cmd([PARSER]))
