"""
Remove command
"""
from .data.gpg_data import remove
from .main import child_parser
from .show import DOCS

@child_parser(DOCS)
def run(args):
    """Removes entry from password db"""
    remove(args.name)
    return 'Removed'
