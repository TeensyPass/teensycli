#!/usr/bin/env python3
"""
Command line interface for Teensy Cli
"""

import argparse
from sys import argv

DESCR = """
Teensy Password
by: Marcell Vazquez-Chanlatte, William Kennington III
"""
EPILOG = """ """

COMMANDS = {'ls', 'insert', 'rm', 'edit', 'generate', 'show'}
HELP = {
    'cmd': ', '.join(COMMANDS),
}

TEENSY_MODULE = 'teensy_pass'

def main():
    """Starts the Teensy CLI"""
    parser = argparse.ArgumentParser(description=DESCR, epilog=EPILOG,
                                     add_help=False)
    parser.add_argument('cmd', nargs=1, default='ls',
            help=HELP['cmd'])

    if len(argv) < 2 or argv[1] not in COMMANDS:
        parser.print_help()
        exit()

    cmd_name = '{0}.{1}'.format(TEENSY_MODULE, argv[1])
    cmd = getattr(__import__(cmd_name, fromlist=[cmd_name]), 'run')
    cmd(parser)

if __name__ == '__main__':
    main()
