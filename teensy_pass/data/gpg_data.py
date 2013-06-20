"""
Wrapper for the data
"""
from os.path import join
from subprocess import check_output
from json import dumps, loads

from ..main import HOME

def save(fname, data, key, home=HOME):
    """ """
    cmd = "echo '{0}' | gpg -ea -r {1}".format(dumps(data), key)
    with open(join(home, fname), 'wb') as filep:
        filep.write(check_output(cmd, shell=True))

def load(fname, home=HOME):
    """ """
    cmd = 'gpg --quiet --no-tty --decrypt {0}'.format(fname)
    with open(join(home, fname), 'r') as filep:
        return loads(check_output(cmd, shell=True).decode('utf-8'))
