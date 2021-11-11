# AOC 2020 Day 23

from os import times
import pathlib
from pprint import pprint
from collections import deque
import time

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day23" / "day23"


def part1(cups):
    for i in range(100):
        current_cup = cups[0]
        cups.rotate(-1)
        cup1 = cups.popleft()
        cup2 = cups.popleft()
        cup3 = cups.popleft()

        # Find next cup
        dest_cup = current_cup - 1

        # while dest_cup not in cups:
        #     dest_cup -= 1
        #     if dest_cup <= 0:
        #         dest_cup = max(cups)
        if dest_cup <= 0:
            dest_cup = 9
        while dest_cup in (cup1, cup2, cup3):
            dest_cup -= 1
            if dest_cup <= 0:
                dest_cup = 9

        # insert the removed cups to the right of the destination
        destination = cups.index(dest_cup)  # + 1
        # cups.insert(destination, cup3)
        # cups.insert(destination, cup2)
        # cups.insert(destination, cup1)
        rotation = (destination + 1) * -1
        cups.rotate(rotation)
        cups.appendleft(cup3)
        cups.appendleft(cup2)
        cups.appendleft(cup1)
        cups.rotate(rotation * -1)

    start = cups.index(1)
    cups.rotate(start * -1)
    cups.popleft()
    return cups


def build_deque(init_list):
    new_cups = deque(init_list, maxlen=1000000)
    for i in range(10, 1000001):
        new_cups.append(i)

    return new_cups


def part2(cups):
    for i in range(10000000):
        if i % 100000 == 0:
            print(f"Round {i}, time: {time.asctime( time.localtime(time.time()) )}")
        current_cup = cups[0]
        cups.rotate(-1)
        cup1 = cups.popleft()
        cup2 = cups.popleft()
        cup3 = cups.popleft()

        # Find next cup
        dest_cup = current_cup - 1
        # while dest_cup not in cups:
        #     dest_cup -= 1
        #     if dest_cup <= 0:
        #         dest_cup = max(cups)
        if dest_cup <= 0:
            dest_cup = 9
        while dest_cup in (cup1, cup2, cup3):
            dest_cup -= 1
            if dest_cup <= 0:
                dest_cup = 9

        # insert the removed cups to the right of the destination
        destination = cups.index(dest_cup)
        # cups.insert(destination, cup3)
        # cups.insert(destination, cup2)
        # cups.insert(destination, cup1)

        rotation = (destination + 1) * -1
        cups.rotate(rotation)
        cups.appendleft(cup3)
        cups.appendleft(cup2)
        cups.appendleft(cup1)
        cups.rotate(rotation * -1)

    start = cups.index(1)
    cups.rotate(start * -1)
    cups.popleft()
    first = cups.popleft()
    second = cups.popleft()
    return first * second


if __name__ == "__main__":

    # My input is 487912365
    cups = deque([4, 8, 7, 9, 1, 2, 3, 6, 5])
    sample_cups = deque([3, 8, 9, 1, 2, 5, 4, 6, 7])
    # pprint(cups)

    print(f"Part 1: Answer: {part1(cups)}")

    cups = build_deque([4, 8, 7, 9, 1, 2, 3, 6, 5])
    # pprint(cups)
    print(f"Part 2: Answer: {part2(cups)}")
