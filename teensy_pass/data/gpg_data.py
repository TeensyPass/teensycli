"""
Wrapper for the data
"""
from os.path import join
from subprocess import check_output
from json import dumps, loads

from ..main import HOME


def save(fname, data, key, home=HOME):
    """Saves the data into fname using the key to encrypt it.
    - fname: Name of the file to save the data into
    - data: Any object that can be dumped into json
    - key: pgp key name
    - home: Base path to save into
    """
    cmd = "echo '{0}' | gpg -ea -r {1}".format(dumps(data), key)
    with open(join(home, fname), 'wb') as filep:
        filep.write(check_output(cmd, shell=True))


def load(fname, home=HOME):
    """Loads the data in fname using pgp to decrypt it.
    - fname: Name of the file to load data from
    - home: Base path of the file
    """
    cmd = 'gpg --quiet --no-tty --decrypt {0}'.format(join(home, fname))
    return loads(check_output(cmd, shell=True).decode('utf-8'))