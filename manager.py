#!/usr/bin/env python3

from json import loads
from getpass import getpass
from os import environ
from gnupg import GPG
import argparse

DESCR = """
Password Manager
by: Marcell Vazquez-Chanlatte
"""
EPILOG = """or you know you could take this by hand..."""
KEY_DSC = """Key that the password is stored under"""


def clean_gpg_json(data):
    return str(data)[2:-1].replace(r'\n', '\n')


def print_pass(passes, key):
    try:
        print(passes[key][1])
    except KeyError:
        print('Invalid Key')


def print_user(passes, key):
    try:
        print(passes[key][0])
    except KeyError:
        print('Invalid Key')


def get_env_vars():
    try:
        return environ['GPG_HOME'], environ['PASS_LOC']
    except KeyError as e:
        print('Environment variables not properly set: {0}'.format(e))
        exit()


def get_passes(gpg_home, pass_loc):
    gpg = GPG(gnupghome=gpg_home)
    with open(pass_loc, mode='rb') as f:
        decoded = gpg.decrypt_file(f, passphrase=getpass())
    if decoded.data == b'':
        print("Incorrect Passphrase")
        exit()
    return loads(clean_gpg_json(decoded.data))


if __name__ == '__main__':
    get_env_vars()
    parser = argparse.ArgumentParser(description=DESCR, epilog=EPILOG)
    parser.add_argument('-k', '--key', dest='key', type=str, help=KEY_DSC)
    parser.add_argument('-l', '--list',  action='store_true')
    parser.add_argument('-p', '--password',  action='store_true')
    parser.add_argument('-u', '--user',  action='store_true')
    args = parser.parse_args()

    passes = get_passes(*get_env_vars())

    if args.list:
        for key in passes.keys(): print(key)
    if args.key is not None:
        if args.password:
            print_pass(passes, args.key)
        if args.user:
            print_user(passes, args.key)
