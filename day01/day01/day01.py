# AOC 2020 Day 1


def part1():

    with open("day01/day01/input", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    for first in numbers:
        second = 2020 - first
        if second in numbers:
            print(f"Part 1: {first} and {second}, product is {first*second}") 

def check_sum(target_sum, first_number, numbers):
    for second in numbers:
        if second != first_number:
            third = target_sum - second
            if third > 0 and third in numbers:
                print(f"Part 2: {first_number}, {second}, and {third}, product is {first_number*second*third}.")
                return True
    return False


def part2():
    with open("day01/day01/input", "r") as f:
        numbers = [int(line) for line in f.readlines()]

    for first in numbers:
        if not check_sum(2020-first, first, numbers):
            print("PROBLEM")


if __name__ == "__main__":
    part1()
    part2()