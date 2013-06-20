"""
Show command
"""
import argparse
from .data.gpg_data import load

DOCS = {
    'name': '',
}

def run(parent):
    """Shows information about a password entry."""
    parser = argparse.ArgumentParser(parents=[parent])
    for opt in DOCS.keys():
        parser.add_argument('-{0}'.format(opt[0]), '--{0}'.format(opt),
                            required=True, help=DOCS[opt])
    args = parser.parse_args()
    data = load(args.name)
    print(data['user'])
    print(data['password'])
