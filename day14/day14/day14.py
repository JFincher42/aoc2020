# AOC 2020 Day 14

import pathlib
from math import pow

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day14" / "day14"


def apply_mask(mask, value):
    # Convert value to 336 binary
    bvalue = bin(value)[2:]
    bvalue = "0" * (36 - len(bvalue)) + bvalue

    new_bvalue = ""
    # Apply the mask
    for i, char in enumerate(mask):
        if char == "X":
            new_bvalue += bvalue[i]
        else:
            new_bvalue += char

    # Convert back to integer
    return int(new_bvalue, base=2)


def part1(lines):

    memory = {}
    mask = "X" * 36

    for line in lines:
        instruction, operand = line.split("=")
        if instruction.strip() == "mask":
            mask = operand.strip()
        else:
            location = int(instruction.strip()[4:-1])
            memory[location] = apply_mask(mask, int(operand.strip()))

    return sum(memory.values())


def generate_address(mask, address):

    # How many X's do we need to replace
    replace_count = mask.count("X")
    max_address = int(pow(2, replace_count))

    for address_mask in range(max_address):

        # Apply the mask to the address
        baddress = bin(address)[2:]
        baddress = "0" * (36 - len(baddress)) + baddress

        new_baddress = ""
        for i, char in enumerate(mask):
            if char == "0" :
                new_baddress += baddress[i]
            else:
                new_baddress += char

        # Now sub in the right bits
        bvalue = bin(address_mask)[2:]
        bvalue = "0" * (replace_count - len(bvalue)) + bvalue
        bit = 0
        new_mask = ""
        for char in new_baddress:
            if char == "X":
                new_mask += bvalue[bit]
                bit += 1
            else:
                new_mask += char

        # Apply the mask
            
        yield int(new_mask, base=2)


def part2(lines):

    memory = {}
    mask = "0" * 36

    for line in lines:
        instruction, operand = line.split("=")
        if instruction.strip() == "mask":
            mask = operand.strip()
        else:
            location = int(instruction.strip()[4:-1])
            for address in generate_address(mask, location):
                memory[address] = int(operand.strip())

    return sum(memory.values())


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
