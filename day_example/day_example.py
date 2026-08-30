"""Day example solution."""

from typing import Literal

from utils import load_puzzle_input

DAY = "example"

def solve(part: Literal["1", "2"]):
    """Day example solution implementation"""
    print(f"Solving day {DAY} part {part}...")
    puzzle_input = get_input()
    raise NotImplementedError()

def get_input():
    """Parse and return puzzle input in desired format."""
    # Return values varies depending on puzzle requirements.
    # Provide specific return type hint for each day.

    # Use util to load file to format list[str].
    puzzle_input = load_puzzle_input(DAY)

    # Parse and return input in desired format here.
    raise NotImplementedError()

if __name__ == "__main__":
    pass
    # Use this block to test solutions.
