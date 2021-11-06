# AOC 2020 Day 20

import pathlib
import pprint

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day20"


class Tile:
    def __init__(self, lines, number):
        self.lines = lines
        self.number = number
        self.neighbors = [None, None, None, None]
        self.block = None
        self.calc_edges()

    def calc_edges(self):
        # Define the edges to start
        self.edges = [0] * 8

        # Get each edge in turn
        # Start with the top edge
        top_edge = ""
        bottom_edge = ""
        left_edge = ""
        right_edge = ""
        for i in range(10):
            if self.lines[0][i] == "#":
                top_edge += "1"
            else:
                top_edge += "0"

            if self.lines[9][i] == "#":
                bottom_edge += "1"
            else:
                bottom_edge += "0"

            if self.lines[i][0] == "#":
                left_edge += "1"
            else:
                left_edge += "0"

            if self.lines[i][9] == "#":
                right_edge += "1"
            else:
                right_edge += "0"

        self.edges[0] = int(top_edge, base=2)
        self.edges[1] = int(bottom_edge, base=2)
        self.edges[2] = int(left_edge, base=2)
        self.edges[3] = int(right_edge, base=2)

        self.edges[4] = int(top_edge[::-1], base=2)
        self.edges[5] = int(bottom_edge[::-1], base=2)
        self.edges[6] = int(left_edge[::-1], base=2)
        self.edges[7] = int(right_edge[::-1], base=2)

    def flip_h(self):
        # Flip this tile top to bottom
        for i in range(5):
            temp = self.lines[i]
            self.lines[i] = self.lines[9 - i]
            self.lines[9 - i] = temp

        # Swap the edges as well, top to bottom
        temp = self.edges[0]
        self.edges[0] = self.edges[1]
        self.edges[1] = temp

        temp = self.edges[4]
        self.edges[4] = self.edges[5]
        self.edges[5] = temp

        # Left to right go to the reversed positions
        temp = self.edges[2]
        self.edges[2] = self.edges[6]
        self.edges[6] = temp

        temp = self.edges[3]
        self.edges[3] = self.edges[7]
        self.edges[7] = temp

    def flip_v(self):
        # Flip this tile left to right
        self.lines = [line[::-1] for line in self.lines]

        # Swap the edges as well, left to right
        temp = self.edges[2]
        self.edges[2] = self.edges[3]
        self.edges[3] = temp

        temp = self.edges[6]
        self.edges[6] = self.edges[7]
        self.edges[7] = temp

        # Top and bottom go to the reversed positions
        temp = self.edges[0]
        self.edges[0] = self.edges[4]
        self.edges[4] = temp

        temp = self.edges[1]
        self.edges[1] = self.edges[5]
        self.edges[5] = temp

    def rotate_c(self):
        # Rotate clockwise
        # Top --> right, right --> bottom
        # Bottom --> left, left --> top

        new_tile = [["." for i in range(10)] for j in range(10)]
        for i in range(10):
            for j in range(10):
                new_tile[j][9 - i] = self.lines[i][j]

        for i in range(10):
            self.lines[i] = "".join(new_tile[i])
        self.calc_edges()

    def rotate_cc(self):
        new_tile = [["." for i in range(10)] for j in range(10)]
        for i in range(10):
            for j in range(10):
                new_tile[9 - j][i] = self.lines[i][j]

        for i in range(10):
            self.lines[i] = "".join(new_tile[i])
        self.calc_edges()

    def __str__(self) -> str:
        tile_str = f"Tile {self.number}:\n"
        # for i in range(10):
        #     tile_str += f"  {self.lines[i]}\n"
        tile_str += f"\n  Top:    {self.edges[0]}, {self.edges[4]}"
        tile_str += f"\n  Bottom: {self.edges[1]}, {self.edges[5]}"
        tile_str += f"\n  Left:   {self.edges[2]}, {self.edges[6]}"
        tile_str += f"\n  Right:  {self.edges[3]}, {self.edges[7]}"
        tile_str += f"\n  NCount: {self.neighbor_count}"
        return tile_str

    def find_neighbors(self, tile):
        for i in range(len(self.edges)):
            if self.edges[i] in tile.edges:
                self.neighbors[i % 4] = tile

    def count_neighbors(self):
        self.neighbor_count = sum([1 for n in self.neighbors if n])

    def inner_block(self):
        """Returns a two-D list of the tile minus the borders"""
        if not self.block:
            self.block = []
            for i in range(1, len(self.lines) - 1):
                block_line = [
                    self.lines[i][x] for x in range(1, len(self.lines[i]) - 1)
                ]
                self.block.append(block_line)

        return self.block


def build_tiles(lines):
    # Keep all the tiles in a list
    tiles = list()

    # Each tile consists of:
    # - a line "Tile ####:"
    # - 10 lines of ten chars
    # - a single blank line
    current_line = 0

    while current_line < len(lines):
        # Parse the first line
        tile_number = int(lines[current_line][5:9])
        current_line += 1
        tile_lines = lines[current_line : current_line + 10]
        current_line += 11
        tiles.append(Tile(tile_lines, tile_number))

    # Now we start looking for matches

    current_tile_index = 0
    while current_tile_index < len(tiles):
        current_tile = tiles[current_tile_index]

        # Loop over every tile
        for tile in tiles:
            # Skip the current tile
            if tile is current_tile:
                continue
            current_tile.find_neighbors(tile)

        current_tile.count_neighbors()
        current_tile_index += 1
    return tiles


def part1(lines):

    tiles = build_tiles(lines)

    # Now we can find the upper left corner
    # It will have two neighbors, right and bottom
    answer = 1
    for tile in tiles:
        if tile.neighbor_count == 2:
            answer *= tile.number

    return answer


def part2(lines):

    # First, build our tiles list
    tiles = build_tiles(lines)

    # Now we can arrange them - find a corner
    top_left_corner = None
    for tile in tiles:
        if tile.neighbor_count == 2:
            top_left_corner = tile
            break

    # Let's get this rotated so the right(3) and bottom edges(1) are populated
    if top_left_corner.neighbors[1] and top_left_corner.neighbors[2]:
        top_left_corner.rotate_cc()
    elif top_left_corner.neighbors[3] and top_left_corner.neighbors[0]:
        top_left_corner.rotate_c()
    elif top_left_corner.neighbors[2] and top_left_corner.neighbors[0]:
        top_left_corner.rotate_c()
        top_left_corner.rotate_c()

    # Let's get the loops working
    i = 0  # start with this row
    j = 0  # and this column
    tile_grid = [[None for i in range(12)] for j in range(12)]
    tile_grid[0][0] = top_left_corner
    tiles.remove(top_left_corner)

    while len(tiles) > 0:
        # Are we looking for the tile to the right, or bottom?
        # i and j are the coordinates of the last set tile
        # if j == 11, we have finished a row, so we look down from i-1,0
        # Otherwise, we look right
        if j == 11:
            match_to_find = tile_grid[i - 1][0].edges[1]
        else:
            match_to_find = tile_grid[i][j].edges[1]

        # Find the tile which matches this one


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    tiles = build_tiles(lines)
    print(f"Tile count = {len(tiles)}")
    pprint.pprint(tiles[0].lines)

    pprint.pprint(tiles[0].inner_block())

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
