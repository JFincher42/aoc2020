# AOC 2020 Day 4

import pathlib
import re

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day04" / "day04"
passport_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
passport_keys1 = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def normalize(lines):
    start = 0
    new_lines = []
    for index in range(len(lines)):
        if len(lines[index]) == 0:
            new_lines.append(" ".join(lines[start:index]))
            start = index + 1
    new_lines.append(" ".join(lines[start : index + 1]))
    return new_lines


def check_byr(data):
    byr = int(data["byr"])
    return byr >= 1920 and byr <= 2002


def check_iyr(data):
    iyr = int(data["iyr"])
    return iyr >= 2010 and iyr <= 2020


def check_eyr(data):
    eyr = int(data["eyr"])
    return eyr >= 2020 and eyr <= 2030


def check_hgt(data):
    hgt = data["hgt"]
    if hgt[-2:] == "cm":
        height = int(hgt[:-2])
        return height >= 150 and height <= 193
    elif hgt[-2:] == "in":
        height = int(hgt[:-2])
        return height >= 59 and height <= 76
    else:
        return False


def check_hcl(data):
    hcl = data["hcl"]
    return len(hcl) == 7 and re.search("#[A-Fa-f0-9]", hcl)


def check_ecl(data):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ecl = data["ecl"]
    return ecl in colors


def check_pid(data):
    pid = data["pid"]
    return len(pid) == 9 and re.search("[0-9]+", pid)


def check_cid(data):
    return True


passport_data_checks = [
    check_byr,
    check_iyr,
    check_eyr,
    check_hgt,
    check_hcl,
    check_ecl,
    check_pid,
    check_cid,
]


def check_data(passport):
    valid = True
    for data_check in passport_data_checks:
        valid = valid and data_check(passport)
        if not valid:
            return 0

    return 1


def check_passport(passport, validate_data):
    for key in passport_keys1:
        if key not in passport.keys():
            return 0

    if validate_data:
        return check_data(passport)
    else:
        return 1


def part1(lines):
    valid_passports = 0

    for line in lines:
        fields = line.split(" ")
        passport = {}
        for field in fields:
            items = field.split(":")
            passport[items[0]] = items[1]
        valid_passports += check_passport(passport, False)

    return valid_passports


def part2(lines):
    valid_passports = 0

    for line in lines:
        fields = line.split(" ")
        passport = {}
        for field in fields:
            items = field.split(":")
            passport[items[0]] = items[1]
        valid_passports += check_passport(passport, True)

    return valid_passports


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    lines = normalize(lines)
    print(f"Part 1: Valid Passports: {part1(lines)}")
    print(f"Part 2: Tree product: {part2(lines)}")
