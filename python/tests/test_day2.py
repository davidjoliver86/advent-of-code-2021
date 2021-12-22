"""
Tests for day 2
"""
from aoc2021 import day2


def test_submarine_movement():
    """
    Test submarine movememnt according to the test case.
    """
    submarine = day2.Submarine()
    for command in ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]:
        submarine.parse_command(command)
    assert (submarine.position, submarine.depth) == (15, 10)


def test_submarine_movement_with_aim():
    """
    Using the second star submarine with aim tracking.
    """
    submarine = day2.SubmarineWithAim()
    for command in ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]:
        submarine.parse_command(command)
    assert (submarine.position, submarine.depth) == (15, 60)


def test_first_star():
    """
    First star solution.
    """
    assert day2.first_star() == 1813801


def test_second_star():
    """
    Second star solution.
    """
    assert day2.second_star() == 1960569556
