# AOC 2020 Day 12

import pathlib


root_path = pathlib.Path.home() / "git" / "aoc2020" / "day12" / "day12"


def part1(directions):

    location = [0, 0]
    moves = {"N": [1, 0], "S": [-1, 0], "E": [0, 1], "W": [0, -1]}
    right_turns = {
        "N": ["E", "S", "W"],
        "E": ["S", "W", "N"],
        "S": ["W", "N", "E"],
        "W": ["N", "E", "S"],
    }
    left_turns = {
        "N": ["W", "S", "E"],
        "E": ["N", "W", "S"],
        "S": ["E", "N", "W"],
        "W": ["S", "E", "N"],
    }

    facing = "E"

    for order in directions:
        if order[0] in "NSEW":
            order_dist = [order[1] * dir for dir in moves[order[0]]]
            location[0] += order_dist[0]
            location[1] += order_dist[1]

        elif order[0] == "F":
            order_dist = [order[1] * dir for dir in moves[facing]]
            location[0] += order_dist[0]
            location[1] += order_dist[1]

        elif order[0] == "R":
            amount = (order[1] // 90) - 1
            facing = right_turns[facing][amount]

        elif order[0] == "L":
            amount = (order[1] // 90) - 1
            facing = left_turns[facing][amount]

    return abs(location[0]) + abs(location[1])


def rotate(vector, amount):

    vectors = [
        [-vector[1], vector[0]],
        [-vector[0], -vector[1]],
        [vector[1], -vector[0]],
    ]

    return vectors[(amount + 4) % 4]


def part2(directions):

    location = [0, 0]
    waypoint = [1, 10]

    moves = {"N": [1, 0], "S": [-1, 0], "E": [0, 1], "W": [0, -1]}

    for order in directions:
        if order[0] in "NSEW":
            order_dist = [order[1] * dir for dir in moves[order[0]]]
            waypoint[0] += order_dist[0]
            waypoint[1] += order_dist[1]

        elif order[0] == "F":
            order_dist = [order[1] * dir for dir in waypoint]
            location[0] += order_dist[0]
            location[1] += order_dist[1]

        elif order[0] == "R":
            amount = (order[1] // 90) - 1
            waypoint = rotate(waypoint, amount)

        elif order[0] == "L":
            amount = 3 - (order[1] // 90)
            waypoint = rotate(waypoint, amount)

    return abs(location[0]) + abs(location[1])


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        directions = [(line[0], int(line[1:])) for line in f.readlines()]

    print(f"Part 1: Distance: {part1(directions)}")
    print(f"Part 2: Number: {part2(directions)}")
