from cipher_hs3240 import cipher_hs3240

import pytest

def test_cipher():
    text = 'd'
    expected = 'c'
    actual = cipher_hs3240.cipher(text, -1)
    assert actual == expected, "Cipher didn't worked."

