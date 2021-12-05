"""
General helper utilities
"""
import pathlib


def ints(path: str) -> list[int]:
    """
    Reads a file and returns a list of its lines cast to integers.

    Args:
        path (str): Path of the file to read.

    Returns:
        list[int]: A list of those lines converted to integers. Blank lines are skipped.
    """
    data = pathlib.Path(path).read_text("utf-8")
    return [int(line) for line in data.splitlines() if line]
