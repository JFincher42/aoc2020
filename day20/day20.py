# AOC 2020 Day 20

import pathlib
import pprint

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day20"

class Tile:
    def __init__(self, lines, number):
        self.lines = lines
        self.number = number
        self.neighbors = [None, None, None, None]
        self.calc_edges()

    def calc_edges(self):
        # Define the edges to start
        self.edges = [0]*8

        # Get each edge in turn
        # Start with the top edge
        top_edge = ""
        bottom_edge = ""
        left_edge = ""
        right_edge = ""
        for i in range(10):
            if self.lines[0][i]=="#":
                top_edge += "1"
            else:
                top_edge += "0"

            if self.lines[9][i]=="#":
                bottom_edge += "1"
            else:
                bottom_edge += "0"

            if self.lines[i][0]=="#":
                left_edge += "1"
            else:
                left_edge += "0"

            if self.lines[i][9]=="#":
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
            self.lines[i] = self.lines[9-i]
            self.lines[9-i] = temp

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

        new_tile = [["."]*10]*10
        for i in range(10):
            for j in range(10):
                new_tile[j][2-i] = self.lines[i][j]

        for i in range(10):
            self.lines[i] = "".join(new_tile[i])
        self.calc_edges()

    def rotate_cc(self):
        new_tile = [["."]*10]*10
        for i in range(10):
            for j in range(10):
                new_tile[2-j][i] = self.lines[i][j]

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
                self.neighbors[i%4] = tile

    def count_neighbors(self):
        self.neighbor_count = sum([1 for n in self.neighbors if n])
        

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
        tile_lines = lines[current_line:current_line+10]
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
    print(len(tiles))

    # Now we can arrange them - find the first corner
    top_left_corner = None
    for tile in tiles:
        if tile.neighbor_count == 2:
            top_left_corner = tile

    # Now we can loop and build the 12x12 tile grid
    tile_grid = [[None]*12]*12





if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]


    tiles = build_tiles(lines)
    pprint.pprint(tiles[0].lines)
    tiles[0].flip_h()
    pprint.pprint(tiles[0].lines)
    tiles[0].flip_v()
    pprint.pprint(tiles[0].lines)
    tiles[0].rotate_c()    
    pprint.pprint(tiles[0].lines)
    tiles[0].rotate_cc()    
    pprint.pprint(tiles[0].lines)


    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
