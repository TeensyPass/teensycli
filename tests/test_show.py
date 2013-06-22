"""
Tests the password show logic
"""
from unittest.mock import patch
from teensy_pass.main import PARSER
from teensy_pass.show import run


@patch('teensy_pass.show.load')
def test_show_run(load):
    load.return_value = dict({'user': 'foo', 'password': 'bar'})
    assert run([PARSER], ['show', '-n', 'doesnt_exist', '-k', 'fake_key']) == \
        'foo\nbar'
