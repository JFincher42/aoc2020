# AOC 2020 Day 17

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day17" / "day17"


def create_neighbors(space):
    new_space = space.copy()

    for coordinates in space.keys():
        for x in range(coordinates[0] - 1, coordinates[0] + 2):
            for y in range(coordinates[1] - 1, coordinates[1] + 2):
                for z in range(coordinates[2] - 1, coordinates[2] + 2):
                    if (x, y, z) not in new_space.keys():
                        new_space[(x, y, z)] = "."

    return new_space


def create_neighbors4(space):
    new_space = space.copy()

    for coordinates in space.keys():
        for x in range(coordinates[0] - 1, coordinates[0] + 2):
            for y in range(coordinates[1] - 1, coordinates[1] + 2):
                for z in range(coordinates[2] - 1, coordinates[2] + 2):
                    for w in range(coordinates[3] - 1, coordinates[3] + 2):
                        if (x, y, z, w) not in new_space.keys():
                            new_space[(x, y, z, w)] = "."

    return new_space


def find_neighbors(coordinates, space):
    neighbors = 0

    for x in range(coordinates[0] - 1, coordinates[0] + 2):
        for y in range(coordinates[1] - 1, coordinates[1] + 2):
            for z in range(coordinates[2] - 1, coordinates[2] + 2):
                if (x, y, z) in space.keys() and space[(x, y, z)] == "#":
                    neighbors += 1

    if space[coordinates] == "#":
        return neighbors - 1
    else:
        return neighbors


def find_neighbors4(coordinates, space):
    neighbors = 0

    for x in range(coordinates[0] - 1, coordinates[0] + 2):
        for y in range(coordinates[1] - 1, coordinates[1] + 2):
            for z in range(coordinates[2] - 1, coordinates[2] + 2):
                for w in range(coordinates[3] - 1, coordinates[3] + 2):
                    if (x, y, z, w) in space.keys() and space[(x, y, z, w)] == "#":
                        neighbors += 1

    if space[coordinates] == "#":
        return neighbors - 1
    else:
        return neighbors


def part1(space):

    space = create_neighbors(space)

    for _ in range(6):
        new_space = space.copy()

        for coordinates, contents in space.items():
            neighbors = find_neighbors(coordinates, space)
            if contents == "#" and neighbors not in [2, 3]:
                new_space[coordinates] = "."

            if contents == "." and neighbors == 3:
                new_space[coordinates] = "#"

        space = create_neighbors(new_space)

    active_cells = 0
    for _, contents in space.items():
        if contents == "#":
            active_cells += 1

    return active_cells


def part2(space):

    space = create_neighbors4(space)
    for _ in range(6):
        new_space = space.copy()

        for coordinates, contents in space.items():
            neighbors = find_neighbors4(coordinates, space)
            if contents == "#" and neighbors not in [2, 3]:
                new_space[coordinates] = "."

            if contents == "." and neighbors == 3:
                new_space[coordinates] = "#"

        space = create_neighbors4(new_space)

    active_cells = 0
    for _, contents in space.items():
        if contents == "#":
            active_cells += 1

    return active_cells


def create_space(lines):
    space = {}

    z = 0
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            space[(x, y, z)] = cell

    return space


def create_space4(lines):
    space = {}

    z = 0
    w = 0
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            space[(x, y, z, w)] = cell

    return space


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    space = create_space(lines)
    space4 = create_space4(lines)

    print(f"Part 1: Answer: {part1(space)}")
    print(f"Part 2: Answer: {part2(space4)}")
