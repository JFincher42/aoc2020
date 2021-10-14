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

def part2(numbers):
    # First, sort the numbers
    numbers.append(0)
    numbers = sorted(numbers)

    # Get the last item
    last_plug = max(numbers)

    # Setup a blank dict to hold the counts
    path_count = dict.fromkeys(numbers, 0)
    path_count[last_plug+3] = 0
    path_count[0] = 1

    # Now we can start to build 
    current_plug = 0

    while current_plug < last_plug:
        if current_plug in numbers:
            current_count = path_count[current_plug]
            if current_plug+1 in numbers:
                path_count[current_plug+1] += current_count
            if current_plug+2 in numbers:
                path_count[current_plug+2] += current_count
            if current_plug+3 in numbers:
                path_count[current_plug+3] += current_count

        current_plug += 1

    return path_count[last_plug]

if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    print(f"Part 1: Number: {part1(numbers)}")
    print(f"Part 2: Number: {part2(numbers)}")
