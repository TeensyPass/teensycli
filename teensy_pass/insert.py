"""
Insert Command
"""
from .data.gpg_data import save
from .main import child_parser

DOCS = {
    'name': '',
    'user': '',
    'password': '',
}

@child_parser(DOCS)
def run(args):
    """Inserts password into the password infrastructure"""
    save(args.name, {'user': args.user, 'password': args.password}, args.key)
    return 'Saved'
