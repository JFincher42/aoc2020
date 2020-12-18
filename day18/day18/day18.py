# AOC 2020 Day 18

import pathlib
from expression import Expression


root_path = pathlib.Path.home() / "git" / "aoc2020" / "day18" / "day18"

def part1(lines):

    sum = 0
    for line in lines:
        expr = Expression(line)
        expr.parse()
        sum += expr.evaluate()

    return sum

def part2(lines):

    sum = 0
    for line in lines:
        expr = Expression(line)
        expr.parse_prec()
        sum += expr.evaluate()

    return sum


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
