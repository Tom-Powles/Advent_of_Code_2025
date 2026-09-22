"""Day 2 solution."""

import pathlib
from typing import Literal

DAY = "2"

def solve(part: Literal["1", "2"]) -> str:
    """Day 2 solution implementation."""
    print(f"Solving day {DAY} part {part}...")
    puzzle_input = get_input(DAY)
    solution = solve_part_1(puzzle_input) if part == "1" else solve_part_2(puzzle_input)
    print(f"...day {DAY}, part {part} solution: {solution}")

def solve_part_1(puzzle_input:list[tuple[int, int]]):
    """
    Sum all ids where int formed from two identical ints
    e.g. 22, 1010, 164164    
    """
    invalid_id_sum = 0

    for start, end in puzzle_input:
        for n in range(start, end + 1):

            # Cast n to str once now.
            # Cast back to int only if all checks pass.
            n = str(n)

            # If len not even, skip immediately.
            if len(n) % 2 != 0:
                continue

            first_half = n[:len(n) // 2]
            second_half = n[len(n) // 2:]
            # print(n, first_half, second_half)

            if first_half == second_half:
                invalid_id_sum += int(n)

    return invalid_id_sum

def solve_part_2(puzzle_input: list[tuple[int, int]]):
    """
    Sum all ids where formed from a sequence of identical integers of any length
    e.g. 555, 2020, 155155155
    """
    invalid_id_sum = 0

    for start, end in puzzle_input:
        for n in range(start, end + 1):

            n = str(n)

            for size in range(1, len(n)):

                # If current size isn't divisible by len(n),
                # skip immediately
                if len(n) % size != 0:
                    continue

                # Sub-divide into size-len parts
                # If all match first, then invalid match
                substrs = []
                for i in range(0, len(n), size):
                    substrs.append(n[i:i + size])

                if all(substrs[0] == substr for substr in substrs):
                    invalid_id_sum += int(n)
                    # Break the inner loop now. Avoid matching
                    # same invalid id multiple times.
                    break

    return invalid_id_sum

def get_input(day: str, sample: bool = False) -> list[tuple[int, int]]:
    """
    Parse and return puzzle input as list of tuples
    contains start and end ints for each range.
    """

    src_path = pathlib.Path(f"day_{day}/day_{day}.txt")
    if sample:
        src_path = pathlib.Path(f"day_{day}/day_{day}_sample.txt")

    if not src_path.exists():
        raise ValueError(f"Cannot find {src_path!s} file.")

    data = []
    with open(src_path, "r", encoding="UTF-8") as f:
        for line in f:
            data.append(line.replace("\n", ""))

    assert len(data) == 1, "More than one line of data."

    str_ranges = data[0].split(",")
    int_ranges = []

    for s_r in str_ranges:
        start, end = s_r.split("-")
        int_ranges.append((int(start), int(end)))

    return int_ranges

if __name__ == "__main__":
    solve("1")
    solve("2")
