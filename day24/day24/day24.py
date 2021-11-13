# AOC 2020 Day 24

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day24" / "day24"


def parse_line(line):
    # Valid directions are:
    # e
    # w
    # ne
    # nw
    # se
    # sw

    i=0
    position = [0, 0]
    while i<len(line):
        if line[i] == "e":
            position[0] += 1
            i += 1
        elif line[i] == "w":
            position[0] -= 1
            i += 1
        elif line[i:i+2] == "ne":
            position[0] += 0.5
            position[1] += 1
            i += 2        
        elif line[i:i+2] == "nw":
            position[0] -= 0.5
            position[1] += 1
            i += 2        
        elif line[i:i+2] == "se":
            position[0] += 0.5
            position[1] -= 1
            i += 2        
        elif line[i:i+2] == "sw":
            position[0] -= 0.5
            position[1] -= 1
            i += 2        
    return position

def part1(lines):
    floor = dict()

    for line in lines:
        tile = parse_line(line)
        tile_id = (tile[0], tile[1])
        if tile_id in floor.keys():
            floor[tile_id] = not floor[tile_id]
        else:
            floor[tile_id] = True

    count = 0
    for val in floor.values():
        if val:
            count += 1

    return count

def part2(lines):

    return -1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]


    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
