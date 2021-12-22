"""
Tests for day 3
"""
from aoc2021 import day3

NUMBERS = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_gamma_and_epsilon():
    """
    Testing the rules for the gamma value and epsilon value.
    """
    gamma, epsilon = day3.find_gamma_and_epsilon(NUMBERS)
    assert (gamma, epsilon) == (22, 9)


def test_filter_criteria_oxygen_generator():
    """
    Testing the criteria for the oxygen_generator function.
    """
    assert day3.filter_criteria(NUMBERS, day3.oxygen_generator) == 23


def test_filter_criteria_co2_scrubber():
    """
    Testing the criteria for the co2_scrubber function.
    """
    assert day3.filter_criteria(NUMBERS, day3.co2_scrubber) == 10


def test_first_star():
    """
    First star solution.
    """
    assert day3.first_star() == 4147524


def test_second_star():
    """
    Second star solution.
    """
    assert day3.second_star() == 3570354
