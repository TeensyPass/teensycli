"""
Wrapper for the data 
"""
from subprocess import check_output
from json import dumps, loads

def save(fname, data, key):
    """ """
    cmd = "echo '{0}' | gpg -ea -r {1}".format(dumps(data), key)
    with open(fname, 'wb') as filep:
        filep.write(check_output(cmd, shell=True))
    
def load(fname):
    """ """
    cmd = 'gpg --quiet --no-tty --decrypt {0}'.format(fname)
    with open(fname, 'r') as filep:
        return loads(check_output(cmd, shell=True).decode('utf-8'))
        
