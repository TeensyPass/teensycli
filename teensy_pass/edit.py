"""
Edit Command
"""
from .data.gpg_data import save, load
from .main import child_parser
from .insert import DOCS

@child_parser(DOCS)
def run(args):
    """Replaces and existing entry with a new one."""
    data = load(args.name)
    data['user'] = args.user
    data['password'] = args.password
    save(args.name, data, args.key)
    return 'Edited'
