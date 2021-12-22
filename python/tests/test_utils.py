"""
Tests for helper functions
"""
from aoc2021 import utils


def test_lines():
    """
    Simple test case for utils.lines with int conversion.
    """
    assert utils.lines("tests/fixtures/utils/ints.txt", int) == [123, 234, 345, 456]
