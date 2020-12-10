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


def count_paths(first, second):
    if first == 1:
        return 0

    if second == 1:
        return first

    return first * second


def part2(numbers):
    complete = set(numbers)
    complete.add(max(numbers) + 3)
    complete.add(0)

    sorted = list(complete)

    diffs = [3]
    for i, plug in enumerate(sorted):
        if i < len(sorted) - 1:
            diffs.append(sorted[i + 1] - plug)

    print(sorted)
    print(diffs)

    i = 0
    single_count = 0
    total = 0
    while i < len(diffs):
        if diffs[i] == 3:
            if single_count>=3:
                total += factorial(single_count) / factorial(single_count - 3)
            else:
                total += single_count
                single_count = 0
        if diffs[i] == 1:
            single_count += 1
        i += 1
    return total

    # path_count = []
    # for plug in complete:
    #     paths = [0,0,0]
    #     for i in range(3):
    #         if plug+i+1 in complete:
    #             paths[i] = 1

    #     if sum(paths) > 0:
    #         path_count.append(sum(paths))

    # print(path_count)
    # # return sum(path_count) + 1
    # # return reduce(count_paths, path_count)

    # final_count = 0
    # for index, path_length in enumerate(path_count):
    #     if path_length == 3:
    #         final_count += path_length * path_count[index+1]
    #     elif path_length == 2:
    #         final_count += path_length

    # return final_count


if __name__ == "__main__":

    with open(root_path / "sample1", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    print(f"Part 1: Number: {part1(numbers)}")
    print(f"Part 2: Number: {part2(numbers)}")
