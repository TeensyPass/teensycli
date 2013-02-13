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

def clean_gpg_json(data):
    return str(data)[2:-1].replace(r'\n', '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCR, epilog=EPILOG)
    parser.add_argument('-k', dest='key', type=str, help=KEY_DSC, required=True)
    args = parser.parse_args()
    gpg = GPG(gnupghome=gpg_home)
    with open(pass_loc, mode='rb') as f:
        decoded = gpg.decrypt_file(f, passphrase=getpass())
    if decoded.data == b'':
        print("Bad Password")
        exit()
    passes = loads(clean_gpg_json(decoded.data))
    print(passes[args.key])
