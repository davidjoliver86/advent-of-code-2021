"""
Tests for helper functions
"""
from aoc2021 import utils


def test_ints():
    """
    Simple test case for utils.ints.
    """
    assert utils.ints("tests/fixtures/utils/ints.txt") == [123, 234, 345, 456]
