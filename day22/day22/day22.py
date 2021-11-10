# AOC 2020 Day 22

import pathlib
from pprint import pprint

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day22"


def score(hand):
    return_score = 0
    multiplier = len(hand)
    for i in range(len(hand)):
        return_score += multiplier * hand[i]
        multiplier -= 1
    return return_score


def part1(hand1, hand2):
    while len(hand1) > 0 and len(hand2) > 0:
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)
        if card1 > card2:
            hand1.append(card1)
            hand1.append(card2)
        else:
            hand2.append(card2)
            hand2.append(card1)

    if len(hand1) > 0:
        return score(hand1)
    else:
        return score(hand2)


def play_rcombat(hand1, hand2):
    while len(hand1) > 0 and len(hand2) > 0:
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)
        # Check if we go to recursive combat here

        # No recursion, so continue here
        if card1 > card2:
            hand1.append(card1)
            hand1.append(card2)
        else:
            hand2.append(card2)
            hand2.append(card1)

    if len(hand1) > 0:
        return (1, hand1)
    else:
        return (2, hand2)


def part2(hand1, hand2):
    _, winning_hand = play_rcombat(hand1, hand2)
    return score(winning_hand)


if __name__ == "__main__":

    with open(root_path / "hand1", "r") as f:
        hand1 = [int(line.strip()) for line in f.readlines()]
    with open(root_path / "hand2", "r") as f:
        hand2 = [int(line.strip()) for line in f.readlines()]

    print(f"Part 1: Answer: {part1(hand1, hand2)}")
    print(f"Part 2: Answer: {part2(hand1, hand2)}")
