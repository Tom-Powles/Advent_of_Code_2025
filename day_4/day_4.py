"""Day 4 solution."""

import pathlib
from typing import Literal, Iterable

DAY = "4"

def solve(part: Literal["1", "2"]):
    """Day 4 solution implementation"""
    print(f"Solving day {DAY} part {part}...")
    puzzle_input = get_input()
    repeat = True if part == "2" else False
    print(f"Day {DAY}, part {part} solution: {_solve(puzzle_input, repeat)}")

def _solve(puzzle_input: list[list[str]], repeat: bool):

    roll_count = 0
    is_rolls_to_remove = True
    rounds = 0

    while is_rolls_to_remove:

        is_rolls_to_remove = False
        rolls_to_remove = _get_rolls_to_remove(puzzle_input)

        if rolls_to_remove:
            rounds += 1
            is_rolls_to_remove = repeat
            puzzle_input = _update_input(puzzle_input, rolls_to_remove)
            roll_count += len(rolls_to_remove)
            print(f"Rounds {rounds}: removed {len(rolls_to_remove)}. Removed {roll_count} total.")
        else:
            print("No more rolls to remove.")

    return roll_count

def _update_input(puzzle_input: list[list[str]], targets: list[tuple[int, int]]) -> list[list[str]]:
    new_input = [inner.copy() for inner in puzzle_input]
    for target in targets:
        new_input[target[0]][target[1]] = "."
    return new_input

def _get_rolls_to_remove(puzzle_input: list[list[str]]) -> list[tuple[int, int]]:
    targets = []
    for outer_idx, outer in enumerate(puzzle_input):
        for inner_idx, _ in enumerate(outer):
            if puzzle_input[outer_idx][inner_idx] != "@":
                continue # skip "."
            sub_grid = _get_sub_grid((outer_idx, inner_idx), puzzle_input, 3)
            all_symbols = [n for l in sub_grid for n in l if n == "@"]
            if len(all_symbols) < 5: # 5 to account for self.
                targets.append((outer_idx, inner_idx))
    return targets

def get_input(day: str = DAY, sample: bool = False) -> list[list[str]]:
    """Parse and return puzzle input in desired format."""
    src_path = pathlib.Path(f"day_{day}/day_{day}.txt")
    if sample:
        src_path = pathlib.Path(f"day_{day}/day_{day}_sample.txt")

    if not src_path.exists():
        raise ValueError(f"Cannot find {src_path!s} file.")

    puzzle_input = []
    with open(src_path, encoding="UTF-8") as f:
        for line in f:
            # Converting to use lists of lists of characters (rather than lists of strings).
            # Updating input required by part 2. String immutability makes that tricky.
            puzzle_input.append(list(line.strip("\n")))
            # input.append(line.strip("\n"))
    return puzzle_input

def _get_sub_grid(coords: tuple[int, int], grid: list[Iterable], size: int):
    """Get sub-grid from larger grid, centred on coords (outer, inner) and of size n."""

    assert size % 2 == 1, "Size not odd number."

    # Calculate fixes values
    offset = (size - 1) // 2
    outer_len = len(grid)
    inner_len = len(grid[0])

    # Work out outer indices
    outer_centre = coords[0]
    outer_min = outer_centre - offset
    outer_min = outer_min if outer_min >= 0 else 0
    outer_max = outer_centre + offset
    outer_max = outer_max if outer_max < outer_len else (outer_len - 1)

    # Work out inner indices
    inner_centre = coords[1]
    inner_min = inner_centre - offset
    inner_min = inner_min  if inner_min >= 0 else 0
    inner_max = inner_centre + offset
    inner_max = inner_max if inner_max < inner_len else (inner_len - 1)

    # It would be easy to reduce the number of variables here.
    # But the current function is fast and easy to debug, so left as-is.

    # Construct sub-grid
    sub_grid = []
    for outer_idx in range(outer_min, outer_max + 1):
        sub_grid.append([
            grid[outer_idx][inner_idx]
            for inner_idx
            in range(inner_min, inner_max + 1)
        ])

    return sub_grid

if __name__ == "__main__":
    solve("1")
    solve("2")
