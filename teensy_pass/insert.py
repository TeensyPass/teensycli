"""
Insert Command
"""
import argparse
import sys
from .data.gpg_data import save

DOCS = {
    'name': '',
    'user': '',
    'password': '',
}


def run(parents, argv=sys.argv):
    """Inserts password into the password infrastructure"""
    parser = argparse.ArgumentParser(parents=parents)
    for opt in DOCS.keys():
        parser.add_argument('-{0}'.format(opt[0]), '--{0}'.format(opt),
                            required=True, help=DOCS[opt])
    args = parser.parse_args(argv)
    save(args.name, {'user': args.user, 'password': args.password}, args.key)
    return 'Saved'
