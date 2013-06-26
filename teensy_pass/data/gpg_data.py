"""
Wrapper for the data
"""
import os
from os import walk
from os.path import join, relpath
from subprocess import check_output
from json import dumps, loads
from functools import wraps

from ..main import HOME


def file_location(func):
    """Combines home and fname -> path"""
    @wraps(func)
    def _file_location(fname, *args, home=HOME, **kwargs):
        return func(join(home, fname), *args, **kwargs)
    return _file_location

    
@file_location
def save(path, data, key):
    """Saves the data into fname using the key to encrypt it.
    - fname: Name of the file to save the data into
    - data: Any object that can be dumped into json
    - key: pgp key name
    - home: Base path to save into
    """
    cmd = "echo '{0}' | gpg -ea -r {1}".format(dumps(data), key)
    with open(path, 'wb') as filep:
        filep.write(check_output(cmd, shell=True))

@file_location
def load(path):
    """Loads the data in fname using pgp to decrypt it.
    - fname: Name of the file to load data from
    - home: Base path of the file
    """
    cmd = 'gpg --quiet --no-tty --decrypt {0}'.format(path)
    return loads(check_output(cmd, shell=True).decode('utf-8'))

    
def list_db(home=HOME):
    """Lists all known passwords
    - home: Base path of the file
    """
    pass_name = lambda base, name: relpath(join(base, name), HOME)
    return '\n'.join(('\n'.join((pass_name(base, name) for name in names))
                      for base, _, names in walk(home)))

    
@file_location    
def remove(path):
    """Removes entry from the database"""
    os.remove(path)
