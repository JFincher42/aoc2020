# AOC 2020 Day 1

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day01" / "day01"


def part1():

    with open(root_path / "input", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    for first in numbers:
        second = 2020 - first
        if second in numbers:
            print(f"Part 1: {first} and {second}, product is {first*second}")
            return

    # If we get here, we have a problem
    print("PROBLEM")
    return


def check_sum(target_sum, first_number, numbers):
    for second in numbers:
        if second != first_number:
            third = target_sum - second
            if third > 0 and third in numbers:
                print(
                    f"Part 2: {first_number}, {second}, and {third}, product is {first_number*second*third}"
                )
                return True
    return False


def part2():
    with open(root_path / "input", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    for first in numbers:
        if check_sum(2020 - first, first, numbers):
            return

    # If we get here, there is a problem
    print("PROBLEM")


if __name__ == "__main__":
    part1()
    part2()