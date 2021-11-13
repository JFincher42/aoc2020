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

    i = 0
    position = [0, 0]
    while i < len(line):
        if line[i] == "e":
            position[0] += 1
            i += 1
        elif line[i] == "w":
            position[0] -= 1
            i += 1
        elif line[i : i + 2] == "ne":
            position[0] += 0.5
            position[1] += 1
            i += 2
        elif line[i : i + 2] == "nw":
            position[0] -= 0.5
            position[1] += 1
            i += 2
        elif line[i : i + 2] == "se":
            position[0] += 0.5
            position[1] -= 1
            i += 2
        elif line[i : i + 2] == "sw":
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


def count_black_tiles(floor, tile_id):
    tiles_mods = [(-1, 0), (1, 0), (-0.5, -1), (-0.5, 1), (0.5, -1), (0.5, 1)]
    count = 0
    for tile_mod in tiles_mods:
        tile = (tile_id[0] + tile_mod[0], tile_id[1] + tile_mod[1])
        if (tile in floor.keys()) and floor[tile]:
            count += 1
    return count


def find_min_max(floor):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    for tile in floor.keys():
        if tile[0] < min_x:
            min_x = tile[0]
        if tile[0] > max_x:
            max_x = tile[0]
        if tile[1] < min_y:
            min_y = tile[1]
        if tile[1] > max_y:
            max_y = tile[1]

    return min_x, max_x, min_y, max_y


def part2(lines):
    floor = dict()
    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    for line in lines:
        tile = parse_line(line)
        tile_id = (tile[0], tile[1])

        # Figure out the extents of the floor
        if tile[0] < min_x:
            min_x = tile[0]
        if tile[0] > max_x:
            max_x = tile[0]
        if tile[1] < min_y:
            min_y = tile[1]
        if tile[1] > max_y:
            max_y = tile[1]

        # Toggle the floor tile
        if tile_id in floor.keys():
            floor[tile_id] = not floor[tile_id]
        else:
            floor[tile_id] = True

    # We do this for 100 days
    for i in range(100):
        # Setup a dict to hold the tiles to change
        new_floor = dict()

        # Now we loop from min to max to figure out what
        # We can't loop over floats, so multiply by 2 to get to integers
        for y in range(int(min_y - 1), int(max_y + 2)):
            for x2 in range(int((min_x - 1.5) * 2), int((max_x + 1.5) * 2), 2):
                x = x2 / 2
                tile_id = (x, y)
                black_tiles = count_black_tiles(floor, tile_id)
                # Have we seen this tile?
                if tile_id in floor.keys():
                    if floor[tile_id]:  # Black tile
                        if black_tiles == 0 or black_tiles > 2:
                            new_floor[tile_id] = not floor[tile_id]  # white
                    else:
                        if black_tiles == 2:
                            new_floor[tile_id] = not floor[tile_id]
                else:
                    # We haven't seen it, so we assume it's a white tile
                    if black_tiles == 2:
                        new_floor[tile_id] = True

        # Add the new floor tiles to original floor
        for tile, value in new_floor.items():
            floor[tile] = value

        # Now we need new min and max vals
        min_x, max_x, min_y, max_y = find_min_max(floor)

        # Count the black tiles
        count = 0
        for val in floor.values():
            if val:
                count += 1

        print(f"Day {i+1}, Black tiles: {count} ")

    # Now we count the black tiles
    count = 0
    for val in floor.values():
        if val:
            count += 1

    return count


if __name__ == "__main__":

    with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
