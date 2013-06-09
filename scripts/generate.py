"""
Generate Command
"""
import argparse
from string import ascii_letters, digits, punctuation
from random import choice

def run(parent):
    """Generates a password"""

    parser = argparse.ArgumentParser(parents=[parent])
    parser.add_argument('length', type=int)
    parser.add_argument('-n', '--no-symbols', dest='no_symbols',
                        action='store_true')
    args = parser.parse_args()

    chars = ascii_letters + digits
    if not args.no_symbols:
        chars += punctuation
    password = ''.join(choice(chars) for _ in range(args.length))
    print(password)
