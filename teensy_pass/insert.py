"""
Insert Command
"""
import argparse
from .data.gpg_data import save

DOCS = {
    'name': '',
    'user': '',
    'password': '',
}

def run(parent):
    """Inserts password into the password infrastructure"""
    parser = argparse.ArgumentParser(parents=[parent])
    for opt in DOCS.keys():
        parser.add_argument('-{0}'.format(opt[0]), '--{0}'.format(opt),
                            required=True, help=DOCS[opt])
    args = parser.parse_args()
    save(args.name, {'user': args.user, 'password': args.password}, args.key)
