# AOC 2020 Day 15

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day15" / "day15"


def part1(numbers, cycles):

    numbers_said = {}

    for turn in range(len(numbers)):
        numbers_said[numbers[turn]] = turn + 1

    for turn in range(len(numbers), cycles):
        if numbers[-1] in numbers[:-1]:
            last_number = turn - numbers_said[numbers[-1]]
        else:
            last_number = 0

        numbers_said[numbers[-1]] = turn 
        numbers.append(last_number)

    return numbers[-1]

def part2(numbers, cycles):
    numbers_said = {}

    for turn in range(len(numbers)-1):
        numbers_said[numbers[turn]] = (1, turn + 1)

    last_number = numbers[-1]

    for turn in range(len(numbers), cycles):

        if last_number in numbers_said.keys():
            last_number_count, last_number_turn = numbers_said[last_number]
            current_number = turn - last_number_turn
        else:
            last_number_count = 0
            last_number_turn = turn
            current_number = 0

        numbers_said[last_number] = (last_number_count+1, turn)
        last_number = current_number

        if not turn % 1000000:
            print(f"Turn {turn}...")

    return last_number

if __name__ == "__main__":

    sample1 = [0, 3, 6]
    sample2 = [1, 3, 2]
    sample3 = [2, 1, 3]
    sample4 = [1, 2, 3]
    sample5 = [2, 3, 1]
    sample6 = [3, 2, 1]
    sample7 = [3, 1, 2]
    final = [14, 8, 16, 0, 1, 17]

    print(f"Part 1: Answer: {part1(final.copy(), 2020)}")
    print(f"Part 2: Answer: {part2(final.copy(), 30000000)}")
