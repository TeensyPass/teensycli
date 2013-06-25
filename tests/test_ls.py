"""
Tests the ls logic
"""
from unittest.mock import patch
from teensy_pass.main import PARSER
from teensy_pass.ls import run

@patch('teensy_pass.ls.list_db')
def test_ls_run(list_db):
    list_db.return_value = "All the directories"
    assert run([PARSER], ['ls'])
