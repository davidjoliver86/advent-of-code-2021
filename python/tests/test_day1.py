"""
Tests for day 1
"""
from aoc2021 import day1, utils


def test_count_increases():
    """
    Simple test case for day1.count_increases().
    """
    ints = utils.ints("tests/fixtures/day1.txt")
    result = day1.count_increases(ints)
    assert result == 7


def test_add_next_two():
    """
    Simple test case for day1.add_next_two().
    """
    ints = utils.ints("tests/fixtures/day1.txt")
    result = day1.add_next_two(ints)
    assert result == [607, 618, 618, 617, 647, 716, 769, 792]


def test_add_next_two_and_count_increases():
    """
    Combines add_next_two() and count_increases().
    """
    ints = utils.ints("tests/fixtures/day1.txt")
    result = day1.count_increases(day1.add_next_two(ints))
    assert result == 5


def test_first_star():
    """
    First star solution.
    """
    assert day1.first_star() == 1832


def test_second_star():
    """
    Second star solution.
    """
    assert day1.second_star() == 1858
