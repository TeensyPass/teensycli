"""
Generate Command
"""
import argparse
from string import ascii_letters, digits, punctuation
from random import choice


def generate_pass(length, no_symbols=False):
    chars = ascii_letters + digits
    if not no_symbols:
        chars += punctuation
    return ''.join(choice(chars) for _ in range(length))


def run(parent):
    """Generates a password"""

    parser = argparse.ArgumentParser(parents=[parent])
    parser.add_argument('length', type=int)
    parser.add_argument('-n', '--no-symbols', dest='no_symbols',
                        action='store_true')
    args = parser.parse_args()
    print(generate_pass(args.length, args.no_symbols))
