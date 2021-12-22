"""
Day 2 : Dive!

Pylint:
    * Ignoring E0601 due to known false-positive with pattern matching with guards.
        * https://github.com/PyCQA/pylint/issues/5327
"""
from aoc2021 import utils


def is_int(val: str) -> bool:
    """
    Parses a string and returns if the value is an integer.

    Args:
        val (str): The string to test.

    Returns:
        bool: If the string represents an integer value.
    """
    try:
        return float(val).is_integer()
    except ValueError:
        return False


class Submarine:
    """
    The submarine is a vessel that can go up, down, or forward.
    """

    position: int = 0
    depth: int = 0

    def parse_command(self, command: str):
        # pylint: disable=E0601
        """
        Parses a direction command and applies the result to the submarines' position or depth.

        Valid commands are in the form of "<up|down|forward> <int>".

        Args:
            command (str): The command to parse.

        Raises:
            ValueError: If an invalid command is passed to parse_command().
        """
        match command.split():
            case ["up", i] if is_int(i):
                self.depth -= int(i)
            case ["down", i] if is_int(i):
                self.depth += int(i)
            case ["forward", i] if is_int(i):
                self.position += int(i)
            case _:
                raise ValueError("Invalid command")


class SubmarineWithAim(Submarine):
    """
    This submarine can aim now. Fancy.
    """

    aim: int = 0

    def parse_command(self, command: str):
        # pylint: disable=E0601
        """
        Parses a direction command and applies the result to the submarines' position, depth, or aim.

        Valid commands are in the form of "<up|down|forward> <int>".

        Args:
            command (str): The command to parse.

        Raises:
            ValueError: If an invalid command is passed to parse_command().
        """
        match command.split():
            case ["up", i] if is_int(i):
                self.aim -= int(i)
            case ["down", i] if is_int(i):
                self.aim += int(i)
            case ["forward", i] if is_int(i):
                val = int(i)
                self.position += val
                self.depth += self.aim * val
            case _:
                raise ValueError("Invalid command")


def first_star() -> int:
    """
    Returns:
        int: Solution for the first star.
    """
    submarine = Submarine()
    for command in utils.lines("fixtures/day2.txt"):
        submarine.parse_command(command)
    return submarine.depth * submarine.position


def second_star() -> int:
    """
    Returns:
        int: Solution for the second star.
    """
    submarine = SubmarineWithAim()
    for command in utils.lines("fixtures/day2.txt"):
        submarine.parse_command(command)
    return submarine.depth * submarine.position


if __name__ == "__main__":
    print(first_star())
    print(second_star())
