# AOC 2020 Day 7

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day08" / "day08"


def acc(ip, acc, operand):
    return ip + 1, acc + operand


def jmp(ip, acc, operand):
    return ip + operand, acc


def nop(ip, acc, operand):
    return ip + 1, acc


jmp_table = {"acc": acc, "jmp": jmp, "nop": nop}


def run(code, ip):
    visited = set()
    acc = 0
    while ip not in visited and ip < len(code):
        visited.add(ip)
        ip, acc = jmp_table[code[ip][0]](ip, acc, code[ip][1])
    return ip in visited, acc


def part1(code, ip):
    looped, acc = run(code, ip)
    return acc


def part2(code, ip):

    # Find every JMP and NOP and swap them, one at a time...
    current_instruction = 0
    while current_instruction < len(code):
        if code[current_instruction][0] == "nop":
            saved_instruction = code[current_instruction]
            code[current_instruction] = ("jmp", code[current_instruction][1])
            loop, acc = run(code, 0)
            if not loop:
                return acc
            code[current_instruction] = saved_instruction

        elif code[current_instruction][0] == "jmp":
            saved_instruction = code[current_instruction]
            code[current_instruction] = ("nop", code[current_instruction][1])
            loop, acc = run(code, 0)
            if not loop:
                return acc
            code[current_instruction] = saved_instruction

        current_instruction += 1


def parse(lines):
    code = []
    for line in lines:
        instructions = line.split(" ")
        code.append((instructions[0], int(instructions[1])))
    return code


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    boot_code = parse(lines)

    print(f"Part 1: Final Acc: {part1(boot_code, 0)}")
    print(f"Part 2: Final Acc: {part2(boot_code, 0)}")
