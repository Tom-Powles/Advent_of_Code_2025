"""Day 3 solution."""
import pathlib
from typing import Literal

DAY = "3"

def solve(part: Literal["1", "2"]):
    """Day 3 solution implementation"""
    print(f"Solving day {DAY} part {part}...")
    puzzle_input = get_input(DAY)
    assert part in ["1", "2"], "Invalid part provided."
    size = 2 if part == "1" else 12
    solution = _solve(puzzle_input, size)
    print(f"Day {DAY}, part {part} solution: {solution}")

def _solve(puzzle_input: list[list[str]], size: int) -> int:
    sum_joltage = 0
    for num in puzzle_input:
        sum_joltage += _get_highest_num(num, size)
    return sum_joltage

def _get_highest_num(n: str, size: int) -> int:

    # Iterative solution is untenable for larger number sizes.
    # Adopting O(n) (where n is number size) logical solution.
    digits = [int(char) for char in n]
    result = []

    for i in range(size, 0, -1):
        # Given available digits, work left-to-right.
        # Record index when highest number first encountered.
        # Digits can be pre-filtered as right-most digits cannot be chosen,
        # based on remaining number size.
        best_idx = None
        best_num = 0
        available_digits = digits[:-(i - 1)] if (i - 1) > 0 else digits
        for idx, num in enumerate(available_digits):
            if num == 9:
                best_idx = idx
                break
            if num > best_num:
                best_idx = idx
                best_num = num
        result.append(digits[best_idx])

        # Cut-off digits left of chosen idx
        digits = digits[best_idx + 1:]

        # Before continuing, check remaining length
        # If too few numbers left, error
        remaining_size = size - len(result)
        assert len(digits) >= remaining_size, "Removed too many digits."

        # If remaining numbers match remaining size,
        # return all remaining digits immediately.
        if len(digits) == remaining_size:
            result.extend(digits)
            break

    return int("".join((str(r) for r in result)))

def get_input(day: str, sample: bool = False) -> list[list[str]]:
    """Parse and return puzzle input in desired format."""
    src_path = pathlib.Path(f"day_{day}/day_{day}.txt")
    if sample:
        src_path = pathlib.Path(f"day_{day}/day_{day}_sample.txt")

    if not src_path.exists():
        raise ValueError(f"Cannot find {src_path!s} file.")

    data = []
    with open(src_path, "r", encoding="UTF-8") as f:
        data = f.readlines()
    return [num.strip("\n") for num in data]

if __name__ == "__main__":
    solve("1")
    solve("2")
