"""
test_caesar
Created February 03, 2022 by Jennifer Baughman

Description:
"""

import pytest
from caesar_cipher import caesar

caesar_input = [[("hellocoders", "encode", 9), "qnuuxlxmnab"],
                [("ilovelucy", "encode", 14), "wzcjsziqm"],
                [("wzcjsziqm", "decode", 14), "ilovelucy"],
                ]


@pytest.mark.parametrize("test_input,expected", caesar_input)
def test_caesar(test_input, expected):
    message, cipher, shift = test_input
    assert caesar(message, cipher, shift) == expected
