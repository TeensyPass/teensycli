"""
Show command
"""
import argparse
import sys
from .data.gpg_data import load

DOCS = {
    'name': '',
}


def run(parents, argv=sys.argv):
    """Returns information about a password entry."""
    parser = argparse.ArgumentParser(parents=parents)
    for opt in DOCS.keys():
        parser.add_argument('-{0}'.format(opt[0]), '--{0}'.format(opt),
                            required=True, help=DOCS[opt])
    args = parser.parse_args(argv)
    data = load(args.name)
    return '\n'.join([data['user'], data['password']])
