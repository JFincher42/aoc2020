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
            top_edge += "1" if self.lines[0][i] == "#" else "0"
            bottom_edge += "1" if self.lines[9][i] == "#" else "0"
            left_edge += "1" if self.lines[i][0] == "#" else "0"
            right_edge += "1" if self.lines[i][9] == "#" else "0"
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
        self.neighbor_count = sum(1 for n in self.neighbors if n)

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
    tiles = []

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

    for tile_ in tiles:
        current_tile = tile_

        # Loop over every tile
        for tile in tiles:
            # Skip the current tile
            if tile is current_tile:
                continue
            current_tile.find_neighbors(tile)

        current_tile.count_neighbors()
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
    # sourcery skip: hoist-statement-from-if, merge-else-if-into-elif, remove-redundant-pass

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

    i += 1

    while len(tiles) > 0:
        # The tile we are currently looking for is (i,j)
        # If i=0, then we're at the start of a row - we need to match what's above us
        #   Which is i-1, j
        # Otherwise, we match what is to the left
        #   Which is i, j-1

        if i==0:
            match_to_find = tile_grid[i][j-1]
            edge_to_find = 1   # Bottom
        else:
            match_to_find = tile_grid[i-1][j]    
            edge_to_find = 3   # Right

        # Find the tile which matches this one
        for tile in tiles:
            if match_to_find.edges[edge_to_find] in tile.edges:
                # Found it!
                # Now to orient it properly
                if edge_to_find == 1:
                    # Make the correct edge the top, 0
                    if match_to_find.edges[edge_to_find] == tile.edges[0]:
                        pass
                    elif match_to_find.edges[edge_to_find] == tile.edges[1]:
                        # Bottom to bottom, flip
                        tile.flip_h()
                    elif match_to_find.edges[edge_to_find] == tile.edges[2]:
                        # Bottom to left, rotate clockwise
                        tile.rotate_c()
                    elif match_to_find.edges[edge_to_find] == tile.edges[3]:
                        # Bottom to right, rotate counter clockwise
                        tile.rotate_cc()
                    elif match_to_find.edges[edge_to_find] == tile.edges[4]:
                        # Bottom to top inverse, flip left to right
                        tile.flip_v()
                    elif match_to_find.edges[edge_to_find] == tile.edges[5]:
                        # Bottom to bottom inverse, rotate twice
                        tile.rotate_c()
                        tile.rotate_c()
                    elif match_to_find.edges[edge_to_find] == tile.edges[6]:
                        # Bottom to left inverse, rotate clockwise and flip
                        tile.rotate_c()
                        #tile.flip_v()
                    elif match_to_find.edges[edge_to_find] == tile.edges[7]:
                        # Bottom to right, rotate counter clockwise and flip
                        tile.rotate_cc()
                        tile.flip_v()

                else:
                    # Make the correct edge the left, 2
                    if match_to_find.edges[edge_to_find] == tile.edges[0]:
                        # Right to top, rotate cc
                        tile.rotate_cc()
                        tile.flip_h()
                    elif match_to_find.edges[edge_to_find] == tile.edges[1]:
                        # Right to bottom, rotate c
                        tile.rotate_c()
                    elif match_to_find.edges[edge_to_find] == tile.edges[2]:
                        # Right to left, pass
                        pass
                    elif match_to_find.edges[edge_to_find] == tile.edges[3]:
                        # Right to right, flip left to right
                        tile.flip_v()
                    elif match_to_find.edges[edge_to_find] == tile.edges[4]:
                        # Right to top inverse, rotate cc and flip
                        tile.rotate_cc()
                        tile.flip_h()
                    elif match_to_find.edges[edge_to_find] == tile.edges[5]:
                        # Right to bottom inverse, rotate c and flip
                        tile.rotate_c()
                        tile.flip_h()
                    elif match_to_find.edges[edge_to_find] == tile.edges[6]:
                        # Right to left inverse, just flip
                        tile.flip_h()
                    elif match_to_find.edges[edge_to_find] == tile.edges[7]:
                        # Right to right inverse, rotate twice
                        tile.rotate_cc()
                        tile.rotate_cc()
                break
        
        tile_grid[i][j] = tile
        match_to_find = tile
        tiles.remove(tile)
        i+=1
        if i>11:
            i=0
            j+=1

    print("Grid built")
        


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    tiles = build_tiles(lines)
    print(f"Tile count = {len(tiles)}")
    pprint.pprint(tiles[0].lines)

    pprint.pprint(tiles[0].inner_block())

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
 