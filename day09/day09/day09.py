# AOC 2020 Day 9

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day09" / "day09"


def find_total(numbers, value):
    for item in numbers:
        if (value - item) in numbers:
            return True
    return False


def part1(numbers, count):

    for index, value in enumerate(numbers[count:], start=count):
        if not find_total(numbers[index - count : index], value):
            return value

    return -1


def part2(numbers, sum_to_find):
    for index, value in enumerate(numbers):
        count = 3
        while sum(numbers[index : index + count]) < sum_to_find:
            count += 1
        if sum(numbers[index : index + count]) == sum_to_find:
            return min(numbers[index : index + count]) + max(
                numbers[index : index + count]
            )

    return -1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    sum_to_find = part1(numbers, 25)
    print(f"Part 1: Number: {sum_to_find}")
    print(f"Part 2: Number: {part2(numbers, sum_to_find)}")
