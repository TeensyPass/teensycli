"""
Tests the password generation system
"""
from teensy_pass.generate import generate_pass
from string import punctuation

def test_generate_pass():
    assert len(generate_pass(3)) == 3
    password = generate_pass(3, no_symbols=True)
    for symbol in punctuation:
        assert symbol not in password
