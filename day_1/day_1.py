"""Fully iterative alternative for troubleshooting."""

from typing import Literal
import pathlib

DAY = "1"

def solve(part: Literal["1", "2"]):
    """Day 1 solution implementation"""
    print(f"Solving day {DAY} part {part}...")
    puzzle_input = get_input()
    zero_count, cycle_count = apply_rotations(puzzle_input)

    # Runs the full calculation for both parts.
    # This is technically wasteful, but a full iteration
    # through all rotations is required either way.
    # Minimal cost for simplicity.
    if part == "1":
        print(f"...day {DAY}, part {part} solution: {zero_count}")
    else:
        print(f"...day {DAY}, part {part} solution: {cycle_count}")

def get_input(day: str = DAY, sample: bool = False) -> list[str]:
    """Parse and return puzzle input in desired format."""
    src_path = pathlib.Path(f"day_{day}/day_{day}.txt")
    if sample:
        src_path = pathlib.Path(f"day_{day}/day_{day}_sample.txt")

    if not src_path.exists():
        raise ValueError(f"Cannot find {src_path!s} file.")

    data = []
    with open(src_path, "r", encoding="UTF-8") as f:
        for line in f:
            data.append(line.replace("\n", ""))
    return data

def parse_rotation(rotation: str) -> int:
    """Convert rotation into numerical change."""
    count = int(rotation[1:])
    direction = rotation[0]

    if direction == "L":
        return count * -1
    if direction == "R":
        return count

    raise ValueError("Rotation direction not 'L' or 'R'.")

def rotate_iter(start: int, change: int) -> tuple[int, int]:
    """
    Alternative iterative approach. Less efficient and not used.  
    """
    number = start
    negative = change < 0
    cycle_count = 0

    for _ in range(abs(change)):

        number += -1 if negative else 1

        if number == -1:
            number = 99

        if number == 100:
            number = 0

        if number == 0:
            cycle_count += 1

    return number, cycle_count

def rotate(start: int, change: int) -> tuple[int, int]:
    """
    Apply a single rotation and return the new number and number of cycles.
    Passing 0 in either direction is a cycle.    
    """
    number = start
    negative = change < 0
    cycle_count = abs(change) // 100
    change_to_apply = abs(change) % 100

    # Flip to negative if originally negative
    if negative:
        change_to_apply = -change_to_apply

    number += change_to_apply

    # Add to cycle count if number ends on 0.
    if number == 0:
        cycle_count += 1

    if negative and number < 0:
        # Do not add to cycle count if start number was 0 and working backwards.
        # This avoids double-counting 0 start/end values.
        if start > 0:
            cycle_count += 1
        number += 100

    if not negative and number > 99:
        cycle_count += 1
        number -= 100

    return number, cycle_count

def apply_rotations(rotations: list[str], start: int = 50) -> tuple[int, int]:
    """
    Apply a sequence of rotations. The default starting position is 50.
    Returns total number of zeros and cycle count.
    """
    number = start
    cycle_count = 0
    zero_count = 0

    for rotation in rotations:
        change = parse_rotation(rotation)
        number, cycles = rotate(number, change)
        cycle_count += cycles

        if number == 0:
            zero_count += 1

    return zero_count, cycle_count

if __name__ == "__main__":
    solve("1")
    solve("2")
