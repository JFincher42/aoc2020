# AOC 2020 Day 1

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day11" / "day11"


def adjacent_seats(seat_grid, row_index, col_index):

    seat_count = 0
    for row in range(row_index - 1, row_index + 2):
        if row >= 0 and row < len(seat_grid):
            for col in range(col_index - 1, col_index + 2):
                if (
                    col >= 0
                    and col < len(seat_grid[row])
                    and (row != row_index or col != col_index)
                ):
                    if seat_grid[row][col] == "#":
                        seat_count += 1

    return seat_count


def visible_seats(seat_grid, row_index, col_index):

    seat_count = 0
    seat_paths = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for seat_path in seat_paths:
        row = row_index + seat_path[0]
        col = col_index + seat_path[1]
        while row in range(len(seat_grid)) and col in range(len(seat_grid[row])):
            if seat_grid[row][col] == "#":
                seat_count += 1
                break
            if seat_grid[row][col] == "L":
                break
            row += seat_path[0]
            col += seat_path[1]

    return seat_count


def part1(seat_grid):

    stable = False
    count = 0

    while not stable:
        new_seat_grid = []
        for row_index, row in enumerate(seat_grid):
            new_row = []
            for col_index, seat in enumerate(row):
                if seat == "L":
                    if adjacent_seats(seat_grid, row_index, col_index) == 0:
                        new_row.append("#")
                    else:
                        new_row.append("L")
                elif seat == "#":
                    if adjacent_seats(seat_grid, row_index, col_index) >= 4:
                        new_row.append("L")
                    else:
                        new_row.append("#")
                else:
                    new_row.append(".")
            new_seat_grid.append("".join(new_row))
        stable = new_seat_grid == seat_grid
        seat_grid = new_seat_grid[:]

    for row in seat_grid:
        count += row.count("#")

    return count


def part2(seat_grid):
    stable = False
    count = 0

    while not stable:
        new_seat_grid = []
        for row_index, row in enumerate(seat_grid):
            new_row = []
            for col_index, seat in enumerate(row):
                if seat == "L":
                    if visible_seats(seat_grid, row_index, col_index) == 0:
                        new_row.append("#")
                    else:
                        new_row.append("L")
                elif seat == "#":
                    if visible_seats(seat_grid, row_index, col_index) >= 5:
                        new_row.append("L")
                    else:
                        new_row.append("#")
                else:
                    new_row.append(".")
            new_seat_grid.append("".join(new_row))
        stable = new_seat_grid == seat_grid
        seat_grid = new_seat_grid[:]

    for row in seat_grid:
        count += row.count("#")

    return count


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        seat_grid = [line.strip() for line in f.readlines()]

    print(f"Part 1: Occupied Seats: {part1(seat_grid)}")
    print(f"Part 2: Number: {part2(seat_grid)}")
