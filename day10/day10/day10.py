# AOC 2020 Day 10

import pathlib
from functools import reduce
from math import factorial

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day10" / "day10"


def part1(numbers):
    complete = set(numbers)
    complete.add(max(numbers) + 3)
    used = set()

    current = 0
    steps = [0, 0, 0]

    while used != complete:
        for i in range(3):
            if current + i + 1 in complete:
                used.add(current + i + 1)
                steps[i] += 1
                current += i + 1
                break

    return steps[0] * steps[2]


def count_paths(numbers, index):

    total_paths = 1
    while index < len(numbers):

        # How many ways out from here
        paths_out = [0,0,0]
        for i in range(3):
            if numbers[index]+i+1 in numbers:
                paths_out[i] = 1

        if sum(paths_out) == 3:
            # Now we need to figure out every path out
            total_paths += count_paths(numbers, index+1)
            total_paths += count_paths(numbers, index+2)
            total_paths += count_paths(numbers, index+3)
            index += 3

        elif sum(paths_out) == 2:
            if paths_out[0]:
                total_paths += count_paths(numbers, index+1)
            if paths_out[1]:
                total_paths += count_paths(numbers, index+2)
            if paths_out[2]:
                total_paths += count_paths(numbers, index+3)
            index += 2

        # Only one way out, just keep looping
        else:
            index += 1

    return total_paths


def part2(numbers):
    numbers.append(0)
    numbers.append(max(numbers)+3)
    numbers.sort()

    return count_paths(numbers, 0)

if __name__ == "__main__":

    with open(root_path / "sample2", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    print(f"Part 1: Number: {part1(numbers)}")
    print(f"Part 2: Number: {part2(numbers)}")
