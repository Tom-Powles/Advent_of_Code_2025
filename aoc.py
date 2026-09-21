"""CLI interface for AOC 2025."""

import argparse
import importlib
import os
import pathlib
import shutil

# pylint: disable=missing-function-docstring

def valid_day(day: str) -> str:
    if 0 < int(day) < 13:
        return day
    raise argparse.ArgumentTypeError("Provided day is invalid. Must be between 1 and 13.")

def _new(day: int) -> None:
    """
    Generate a folder for X day using `day_example`
    where one doesn't already exist.
    """
    # Create new directory and copy files from day_example directory, renaming "example" to "day"
    if os.path.exists(f"day_{day}/"):
        print("Folder already exists. Delete it and re-run to recreate from example template.")
        return

    src_path = pathlib.Path("day_example")
    new_path = pathlib.Path(f"day_{day}")
    os.mkdir(new_path)

    for file in src_path.iterdir():
        shutil.copy(file, new_path / file.name.replace("example", str(day)))

def _show(day: int) -> None:
    """Show the puzzle description for X day."""
    with open(f"day_{day}/day_{day}.md", encoding="UTF-8") as f:
        print(f.read())

def _solve(day: int) -> None:
    """Calculate and display solutions (parts 1 and 2) for X day."""
    try:
        solver = importlib.import_module(f"day_{day}.day_{day}")
    except ModuleNotFoundError:
        print(f"No solution for day {day} found. Does day_{day}/day_7.py exist? " \
              "Create a template for building a solution by running: python aoc.py new {day}")
        return

    try:
        solver.solve("1")
        solver.solve("2")
    except NameError:
        print(f"No 'solve' function found in day_{day}.py."\
              "This function is required to run solutions.")


if __name__ == "__main__":

    # Using argparse library for minimal CLI
    # Limited but avoids dependencies for such a basic use case.
    parser = argparse.ArgumentParser(
        prog="Advent of Code 2025 solver",
        description="Problem descriptions, puzzle input," \
        "and solutions for Advent of Code 2025: https://adventofcode.com/2025."
        )

    # Mode argument determines whether we're running a solution, displaying puzzle input etc.
    parser.add_argument(
        "mode",
        choices=["new", "show", "solve"],
        help=f"Available modes:\n 1.) new: {_new.__doc__.strip()}\n"
            f"2.) show: {_show.__doc__}\n"
            f"3.) solve: {_solve.__doc__}\n")
    parser.add_argument("day", type=valid_day, help="A puzzle day. A number between 1 and 12.")

    args = parser.parse_args()

    # Run by using mode to identify function.
    # Functions stored in dict returned by globals() function call.
    globals()[f"_{args.mode}"](args.day)
