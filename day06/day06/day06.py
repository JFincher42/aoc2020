# AOC 2020 Day 6

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day06" / "day06"


def part1(lines):
    answer_count = 0
    index = 0
    while index <= len(lines):
        questions = set()
        line = lines[index]
        while line:
            questions = questions | set(line)
            index += 1
            if index < len(lines):
                line = lines[index]
            else:
                line = ""
        answer_count += len(questions)
        index += 1

    return answer_count


def part2(lines):
    answer_count = 0
    index = 0
    while index <= len(lines):
        line = lines[index]
        questions = set(line)
        while line:
            questions = questions & set(line)
            index += 1
            if index < len(lines):
                line = lines[index]
            else:
                line = ""
        answer_count += len(questions)
        index += 1

    return answer_count


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer Count: {part1(lines)}")
    print(f"Part 2: Answer Count: {part2(lines)}")
