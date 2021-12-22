"""
Day 3: Binary Diagnostic
"""
from typing import Callable, Tuple
from functools import lru_cache

from aoc2021 import utils

BitCounts = dict[str, int]
BitCriteria = list[BitCounts]


class UnexpectedAnswer(Exception):
    """
    Covers unexpected scenarios.
    """


def get_digit_counts(numbers: list[str]) -> BitCriteria:
    """
    From a list of identically-sized binary numbers represented as strings, create and return a
    list of dictionaries representing the counts of each digit in each of the respective places
    in the number.

    Args:
        numbers (list[str]): List of binary numbers represented as strings.

    Returns:
        BitCriteria: A list of dictionaries representing digit counts in each space. For example:
        [{"0": 3, "1": 1}, {"0": 1, "1": 3},...]
    """
    digit_counts = [{} for digit in numbers[0]]
    for number in numbers:
        for position, digit in enumerate(number):
            digit_counts[position][digit] = digit_counts[position].get(digit, 0) + 1
    return digit_counts


def find_gamma_and_epsilon(numbers: list[str]) -> Tuple[int, int]:
    """
    In a list of a sequence of binary numbers of the same bitsize, we want to find the "gamma rate"
    and "epsilon rate". For each bit position, if there were more 1's than 0's, that becomes a '1'
    in that bit of the gamma rate and '0' in the epsilon rate. And vice versa - if there were more 0's,
    that bit in epsilon is a '1' and in gamma is a '0'.

    We find the Gamma and Epsilon values at the same time because they're derived from the same
    method of computation.

    Args:
        numbers (list[str]): A list of strings representing binary numbers.

    Returns:
        Tuple[int, int]: The gamma and epsilon values, respectively.
    """
    digit_counts = get_digit_counts(numbers)
    gamma, epsilon = (0, 0)
    bit_count = len(digit_counts)
    for index, counts in enumerate(digit_counts):
        bits_to_shift = bit_count - 1 - index
        if counts["0"] > counts["1"]:
            epsilon ^= 1 << bits_to_shift
        elif counts["1"] > counts["0"]:
            gamma ^= 1 << bits_to_shift
        else:
            raise UnexpectedAnswer("0's and 1's are equal. This probably should not happen.")
    return gamma, epsilon


# Helper functions for Oxygen Generator and CO2 Scrubber ratings


def oxygen_generator(counts: BitCounts) -> str:
    """
    The oxygen generator bit criteria is to keep the most common occuring value.

    Args:
        counts (BitCounts): The counts for this particular digit.

    Returns:
        str: "0" if 0's are most common, "1" if 1's are most or equally common.
    """
    if counts["0"] > counts["1"]:
        return "0"
    if counts["1"] > counts["0"]:
        return "1"
    return "1"


def co2_scrubber(counts: BitCounts) -> str:
    """
    The CO2 scrubber bit criteria is to keep the least common occuring value.

    Args:
        counts (BitCounts): The counts for this particular digit.

    Returns:
        str: "0" if 0's are least or equally common, "1" if 1's are most common.
    """
    if counts["0"] < counts["1"]:
        return "0"
    if counts["1"] < counts["0"]:
        return "1"
    return "0"


def filter_criteria(numbers: list[str], criteria: Callable[[BitCounts], str], index: int = 0) -> int:
    """
    Takes a list of binary numbers as strings. A criteria function will then apply rules to filter
    this list down based on the digit position represented by index.

    If the filtering results in two or more numbers remaining, recursively call this again on that
    list, proceeding to the next index position.

    The solutions are designed such that this should always result in one remaining number at a
    certain point. If so, convert that number to decimal and return it.

    In theory, this can raise IndexError if the filtering doesn't whittle the list down to exactly
    one element.

    Args:
        numbers (list[str]): The list of binary numbers as strings.
        criteria (Callable[[BitCounts], str]): A test function to apply a filtering rule.
        index (int, optional): Index of the digit for filtering. Defaults to 0.

    Raises:
        IndexError: If the filtering does not result in a numbers list length of 1.

    Returns:
        int: The binary-to-decimal result of the one remaining list element.
    """
    # If one number remains, convert that from binary to decimal and return it.
    if len(numbers) == 1:
        val = 0
        bit_count = len(numbers[0])
        for winner_index, digit in enumerate(numbers[0]):
            bits_to_shift = bit_count - 1 - winner_index
            if digit == "1":
                val ^= 1 << bits_to_shift
        return val
    digit_counts = get_digit_counts(numbers)
    digit_to_keep = criteria(digit_counts[index])
    filtered_numbers = [number for number in numbers if number[index] == digit_to_keep]
    return filter_criteria(filtered_numbers, criteria, index + 1)


@lru_cache
def _read_values():
    """
    Reads the fixtures from the puzzle input.
    """
    return utils.lines("fixtures/day3.txt")


def first_star():
    """
    Returns:
        int: Solution for the first star.
    """
    gamma, epsilon = find_gamma_and_epsilon(_read_values())
    return gamma * epsilon


def second_star():
    """
    Returns:
        int: Solution for the second star.
    """
    numbers = _read_values()
    oxygen = filter_criteria(numbers, oxygen_generator)
    co2 = filter_criteria(numbers, co2_scrubber)
    return oxygen * co2


if __name__ == "__main__":
    print(first_star())
    print(second_star())
