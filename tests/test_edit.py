"""
Tests the password insert logic
"""
from unittest.mock import patch
from teensy_pass.main import PARSER
from teensy_pass.edit import run


@patch('teensy_pass.edit.save')
@patch('teensy_pass.edit.load')
def test_edit_run(load, save):
    load.return_value = dict({'user': 'foo', 'password': 'bar'})
    assert run([PARSER], ['edit', '-n', 'name', '-u', 'foo', '-p', 'bar',
                          '-k', 'fake_key']) == 'Edited'
    data = {'user': 'foo', 'password': 'bar'}
    save.assert_called_with('name', data, 'fake_key')
