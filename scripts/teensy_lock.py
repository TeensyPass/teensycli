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

COMMANDS = {'ls', 'insert', 'rm', 'edit', 'generate', 'show'}
HELP = {
    'cmd': ', '.join(COMMANDS),
}


def main():
    """Starts the Teensy CLI"""
    parser = argparse.ArgumentParser(description=DESCR, epilog=EPILOG)
    parser.add_argument('cmd', nargs='*', default=['ls'], help=HELP['cmd'])
    args = parser.parse_args()

    # load the correct command based on the the command name
    if args.cmd[0] not in COMMANDS:
        print('Invalid command\n')
        parser.print_help()
        exit()
    cmd = getattr(__import__(args.cmd[0], fromlist=[args.cmd[0]]), 'run')
    cmd(args)

if __name__ == '__main__':
    main()
