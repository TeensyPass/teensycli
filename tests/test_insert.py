"""
Tests the password insert logic
"""
from unittest.mock import patch
from teensy_pass.main import PARSER
from teensy_pass.insert import run


@patch('teensy_pass.insert.save')
def test_insert_run(save):
    assert run([PARSER], ['insert', '-n', 'name', '-u', 'foo', '-p', 'bar',
                          '-k', 'fake_key']) == 'Saved'
    data = {'user': 'foo', 'password': 'bar'}
    save.assert_called_with('name', data, 'fake_key')
