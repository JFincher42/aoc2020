# AOC 2020 Day 4

import pathlib
import re

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day04" / "day04"
passport_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
passport_keys1 = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def normalize(lines):
    """Normalize raw input to make it easier to read later

    Args:
        lines (list): A list of lines read raw from the input file

    Returns:
        list: Input lines concatenated with blanks removed
    """

    # Where do we start
    start = 0
    new_lines = []

    # Loop through the entire list of lines
    for index in range(len(lines)):
        # When we find a blank line
        if len(lines[index]) == 0:
            # Concat everything from the start to the line before
            new_lines.append(" ".join(lines[start:index]))
            # New start is the next line
            start = index + 1

    # We need to catch the last few lines when we get to the end
    new_lines.append(" ".join(lines[start : index + 1]))
    return new_lines


# Data Validators
# Each of the following functions takes one parameter:
# - data: a dictionary containing all required keys
# It returns True if the data conforms to spec, False otherwise
def check_byr(data):
    byr = data["byr"]
    return (
        re.search("[0-9]+", byr)
        and len(byr) == 4
        and int(byr) >= 1920
        and int(byr) <= 2002
    )


def check_iyr(data):
    iyr = data["iyr"]
    return (
        re.search("[0-9]+", iyr)
        and len(iyr) == 4
        and int(iyr) >= 2010
        and int(iyr) <= 2020
    )


def check_eyr(data):
    eyr = data["eyr"]
    return (
        re.search("[0-9]+", eyr)
        and len(eyr) == 4
        and int(eyr) >= 2020
        and int(eyr) <= 2030
    )


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


# Put all the data checks in a list so we can call them in turn
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
    """Validates the data in a given passport

    Args:
        passport (dict): Keys and values describing a passport

    Returns:
        int: 1 if all the passport data is valid, 0 if not
    """

    # Assume everything is good
    valid = True

    # Loop through each check
    for data_check in passport_data_checks:
        # Run the check and collate into valid
        valid = valid and data_check(passport)

        # If we are ever invalid, return 0 - no more checks needed
        if not valid:
            return 0

    # Everything passed
    return 1


def check_passport(passport, validate_data):
    """Checks a passport for validity

    Args:
        passport (dict): Keys and value describing a passport
        validate_data (bool): Should we validate the data as well?

    Returns:
        int: 1 if the passport is valid, 0 otherwise
    """

    # Look at every key required for a valid passport
    for key in passport_keys1:
        # Does this key exist in the passport? If not, it's invalid
        if key not in passport.keys():
            return 0

    # The passport has all required keys, do we check the data?
    if validate_data:
        return check_data(passport)

    # If no data check, then the passport is valid
    else:
        return 1


def get_passport(line):
    """Generates a passport given a string of data

    Args:
        line (string): A string containing passport data.

    Returns:
        dict : a dictionary with parsed passport data
    """

    # Each passport is a set of key/value pairs separated by spaces
    fields = line.split(" ")
    passport = {}

    # Each field is a key and value, separated by a colon (:)
    for field in fields:
        items = field.split(":")
        passport[items[0]] = items[1]

    return passport


def part1(lines):

    # How many valid passports do we have
    valid_passports = 0

    # Every line contains one passport
    for line in lines:
        passport = get_passport(line)
        # Once we have the data parsed, check if it's valid
        # No data check on for part 1
        valid_passports += check_passport(passport, False)

    return valid_passports


def part2(lines):
    # How many valid passports do we have
    valid_passports = 0

    # Every line contains one passport
    for line in lines:
        passport = get_passport(line)
        # Once we have the data parsed, check if it's valid
        # Data check required for part 2
        valid_passports += check_passport(passport, True)

    return valid_passports


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    lines = normalize(lines)
    print(f"Part 1: Valid Passports: {part1(lines)}")
    print(f"Part 2: Tree product: {part2(lines)}")
