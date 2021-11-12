# AOC 2020 Day 24

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day24"


def part1(lines):

    return -1

def part2(lines):

    return -1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]


    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
