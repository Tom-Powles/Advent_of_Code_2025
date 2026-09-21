"""Day example solution."""

import pathlib
from typing import Literal

DAY = "example"

def solve(part: Literal["1", "2"]):
    """Day example solution implementation"""
    print(f"Solving day {DAY} part {part}...")
    puzzle_input = get_input()
    raise NotImplementedError()

def get_input(day: str = DAY, sample: bool = False) -> list[str]:
    """Parse and return puzzle input in desired format."""
    # Return values varies depending on puzzle requirements.
    # Provide specific return type hint for each day.
    src_path = pathlib.Path(f"day_{day}/day_{day}.txt")
    if sample:
        src_path = pathlib.Path(f"day_{day}/day_{day}_sample.txt")

    if not src_path.exists():
        raise ValueError(f"Cannot find {src_path!s} file.")

    data = []
    with open(src_path, "r", encoding="UTF-8") as f:
        for line in f:
            data.append(line.replace("\n", ""))

    # Optionally add required data transformation(s) here.

    return data

if __name__ == "__main__":
    pass
    # Use this block to test solutions.
