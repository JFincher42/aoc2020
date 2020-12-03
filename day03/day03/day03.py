# AOC 2020 Day 3

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day03" / "day03"


def count_trees(lines, right, down):
    # Where are we on the slope?
    pos_x, pos_y = 0, 0

    # How many trees have we hit?
    trees = 0

    # While we're not at the bottom
    while pos_y < len(lines):
        # Check the current location
        if lines[pos_y][pos_x] == "#":
            trees += 1

        # Update the location
        pos_x = (pos_x + right) % len(lines[pos_y])
        pos_y += down

    return trees


def part1(lines):
    return count_trees(lines, 3, 1)


def part2(lines):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = 1
    for slope in slopes:
        trees *= count_trees(lines, slope[0], slope[1])

    return trees


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Trees: {part1(lines)}")
    print(f"Part 2: Tree product: {part2(lines)}")
