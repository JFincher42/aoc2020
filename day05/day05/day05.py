# AOC 2020 Day 5

import pathlib
import pprint

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day05" / "day05"
subs = {"F": "0", "B": "1", "R": "1", "L": "0"}


def get_number(code):
    number = "".join([subs[letter] for letter in code])
    return int(number, base=2)


def part1(lines):
    highest_seat_id = 0

    for line in lines:
        row = get_number(line[0:7])
        seat = get_number(line[-3:])
        seat_id = row * 8 + seat
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id


def part2(lines):
    seat_ids = []
    for line in lines:
        row = get_number(line[0:7])
        seat = get_number(line[-3:])
        seat_ids.append(row * 8 + seat)

    seat_ids.sort()
    current_seat = seat_ids[0]
    for next_seat in seat_ids[1:]:
        if next_seat == current_seat+1:
            current_seat = next_seat
        else:
            return next_seat-1

    return -1

if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Highest Seat: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
