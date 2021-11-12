# AOC 2020 Day 25

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day25" / "day25"


def find_loop(pk):
    sn = 7
    loop = 0
    val = 1

    while val != pk:
        val *= sn
        val %= 20201227
        loop += 1

    return loop


def transform(sn, loop):
    val = 1
    for _ in range(loop):
        val *= sn
        val %= 20201227

    return val


def part1(cpk, dpk):
    card_loop = find_loop(cpk)
    door_loop = find_loop(dpk)
    return transform(cpk, door_loop)


def part2(cpk, dpk):
    return -1


if __name__ == "__main__":

    card_public_key = 11562782
    door_public_key = 18108497

    sample_card_public_key = 5764801
    sample_door_public_key = 17807724

    print(f"Part 1: Answer: {part1(card_public_key, door_public_key)}")
    # print(f"Part 1: Answer: {part1(sample_card_public_key, sample_door_public_key)}")
    print(f"Part 2: Answer: {part2(card_public_key, door_public_key)}")
    # print(f"Part 2: Answer: {part2(sample_card_public_key, sample_door_public_key)}")
