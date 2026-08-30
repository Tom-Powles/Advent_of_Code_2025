"""Common functions."""

import pathlib

def load_puzzle_input(day: str) -> list[str]:
    """Load puzzle inputs from .txt files to standard list[str] format."""

    src_path = pathlib.Path(f"day_{day}/day_{day}.txt")
    if not src_path.exists():
        raise ValueError(f"For day {day!s} cannot find day_{day}.txt file.")

    with open(src_path, "r", encoding="UTF-8") as f:
        return f.readlines()

if __name__ == "__main__":

    try:
        load_puzzle_input("15")
    except ValueError as e:
        print(f"Failed to find .txt file with error: {e}")

    test_input = load_puzzle_input("1")
    print(f"Loaded day 1 input with {len(test_input)} lines.")
