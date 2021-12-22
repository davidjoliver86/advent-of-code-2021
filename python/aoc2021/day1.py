"""
Day 1: Sonar Sweep
"""
from typing import Sequence
from . import utils


def count_increases(ints: Sequence[int]) -> int:
    """
    Args:
        ints (Sequence[int]): The sequence of integers to evaluate.

    Returns:
        int: The number of occurrences in the sequence where one element was greater than the previous.
    """
    increases = 0
    previous = ints[0]
    for current in ints[1:]:
        if current > previous:
            increases += 1
        previous = current
    return increases


def add_next_two(ints: Sequence[int]) -> list[int]:
    """
    Returns a new list where each element is equal to itself plus the next two elements of that list. The returned list
    will be two elements shorter than the input list.

    Example:
        add_next_two([1, 2, 3, 4, 5]) => [6, 9, 12]

    Args:
        ints (Sequence[int]): The sequence of integers to sum their next two values.

    Returns:
        list[int]: A new list with each element equal to old[i] + old[i+1] + old[i+2].
    """
    return [(ints[i] + ints[i + 1] + ints[i + 2]) for i in range(len(ints) - 2)]


def first_star() -> int:
    """
    Returns:
        int: Solution for the first star.
    """
    return count_increases(utils.lines("fixtures/day1.txt", int))


def second_star() -> int:
    """
    Returns:
        int: Solution for the second star.
    """
    return count_increases(add_next_two(utils.lines("fixtures/day1.txt", int)))


if __name__ == "__main__":
    print(first_star())
    print(second_star())
