"""
Tests the password gpg_data logic
"""
from os.path import join
from unittest.mock import patch, MagicMock
from teensy_pass.data.gpg_data import save, load, list_db


@patch('teensy_pass.data.gpg_data.check_output')
@patch('teensy_pass.data.gpg_data.dumps')
@patch('builtins.open')
def test_save(open, dumps, check_output):
    dumps.return_value = ''
    save('foo', {'bar': 'foo'}, 'key', 'home')
    check_output.assert_called_with("echo '' | gpg -ea -r key", shell=True)
    open.assert_called_with(join('home', 'foo'), 'wb')
    dumps.assert_called_with({'bar': 'foo'})

@patch('teensy_pass.data.gpg_data.check_output')    
@patch('teensy_pass.data.gpg_data.loads')    
@patch('builtins.open')
def test_load(open, loads, check_output):
    loads.return_value = 'this is the end'
    assert load('foo', 'home') == 'this is the end'
    cmd = 'gpg --quiet --no-tty --decrypt {0}'.format(join('home', 'foo'))
    check_output.assert_called_with(cmd, shell=True)

@patch('teensy_pass.data.gpg_data.walk')
def test_list_db(walk):
    walk.return_value = [('foo', 'arg', ['file1', 'file2']),
                         ('.', 'fdsf', ['file3', 'file4'])]
    assert list_db(home='home') == 'foo/file1\nfoo/file2\nfile3\nfile4'
    
