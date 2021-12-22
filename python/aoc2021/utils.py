"""
General helper utilities
"""
import pathlib
from typing import Any, Callable


def lines(path: str, func: Callable = None) -> list[Any]:
    """
    Reads a file and returns a list of its lines. Optionally accepts a calllable, and if provided,
    applies that callable to all lines.

    Args:
        path (str): Path of the file to read.
        func (Callable, optional): Function to apply to each line (takes one argument). Defaults to None.

    Returns:
        list[Any]: A list of those lines. Blank lines are skipped.
    """
    data = pathlib.Path(path).read_text("utf-8")
    if func:
        return [func(line) for line in data.splitlines() if line]
    return [line for line in data.splitlines() if line]
