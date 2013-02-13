#!/usr/bin/env python3

from json import loads
from getpass import getpass
from os import environ
from gnupg import GPG
import argparse

gpg_home = environ['GPG_HOME']
pass_loc = environ['PASS_LOC']

DESCR = """
Password Manager
by: Marcell Vazquez-Chanlatte
"""
EPILOG = """or you know you could take this by hand..."""
KEY_DSC = """Key that the password is stored under"""

def load_keys(func):
    def _load_keys(*args, **kwargs):
        gpg = GPG(gnupghome=gpg_home)
        with open(pass_loc, mode='rb') as f:
            decoded = gpg.decrypt_file(f, passphrase=getpass())
        if decoded.data == b'':
            exit()
        passes = loads(clean_gpg_json(decoded.data))
        func(passes, *args)
    return _load_keys


def clean_gpg_json(data):
    return str(data)[2:-1].replace(r'\n', '\n')

@load_keys
def list_keys(passes, *args):
    for key in passes.keys():
        print(key)

@load_keys
def print_key(passes, key):
    print(passes[key])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCR, epilog=EPILOG)
    parser.add_argument('-k', '--key', dest='key', type=str, help=KEY_DSC)
    parser.add_argument('-l', '--list',  action='store_true')
    args = parser.parse_args()
    if args.list:
        list_keys()
    if args.key is not None:
        print_key(args.key)
