#!/usr/env python3

from json import loads
from getpass import getpass
from os import environ
from gnupg import GPG

gpg_home = environ['GPG_HOME']
pass_loc = environ['PASS_LOC']

def clean_gpg_json(data):
    return str(data)[2:-1].replace(r'\n', '\n')


if __name__ == '__main__':
    gpg = GPG(gnupghome=gpg_home)
    with open(pass_loc, mode='rb') as f:
        decoded = gpg.decrypt_file(f, passphrase=getpass())
    if decoded.data == b'':
        print("Bad Password")
        exit()
    passes = loads(clean_gpg_json(decoded.data))
    print(passes['www.google.com'])
