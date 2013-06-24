"""
Show command
"""

from .data.gpg_data import load
from .main import child_parser

DOCS = {
    'name': '',
}

@child_parser(DOCS)
def run(args):
    """Returns information about a password entry."""
    data = load(args.name)
    return '\n'.join([data['user'], data['password']])
