# AOC 2020 Day 2

import pathlib, collections

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day02" / "day02"


def part1(lines):

    valid_count = 0

    for line in lines:
        hilo, letter, password = line.split(" ")

        # Get extents
        lo, hi = hilo.split("-")
        lo, hi = int(lo), int(hi)

        # Isolate letter
        letter = letter[0]

        # Count the letters in the password
        letter_count = collections.Counter(password)

        if letter_count[letter] >= lo and letter_count[letter] <= hi:
            valid_count += 1

    return valid_count


def part2(lines):
    valid_count = 0

    for line in lines:
        hilo, letter, password = line.split(" ")

        # Get extents
        lo, hi = hilo.split("-")
        lo, hi = int(lo)-1, int(hi)-1

        # Isolate letter
        letter = letter[0]

        if len(password) >= hi:
            if password[lo] == letter or password[hi] == letter:
                if not (password[lo] == letter and password[hi] == letter):
                    valid_count += 1

    return valid_count


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Valid passwords: {part1(lines)}")
    print(f"Part 2: Valid passwords: {part2(lines)}")
