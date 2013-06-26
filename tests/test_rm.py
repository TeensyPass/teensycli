"""
Tests the password removal logic
"""
from unittest.mock import patch
from teensy_pass.main import PARSER
from teensy_pass.rm import run

@patch('teensy_pass.rm.remove')
def test_show_run(remove):
    assert run([PARSER], ['rm', '-n', 'name', '-k', 'fake_key']) == 'Removed'
    remove.assert_called_with('name')
