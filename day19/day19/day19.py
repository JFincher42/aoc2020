# AOC 2020 Day 18

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day19" / "day19"


def part1(lines):

    return -1


def part2(lines):

    return -1


def parse_rules(lines):

    rules = {}

    index = 0
    while lines[index]:
        rule_number, production_string = lines[index].split(":")
        products = []
        products_string = production_string.split("|")
        for product_rule in products_string:
            product_rule = product_rule.strip()
            if '"' in product_rule:
                products.append(product_rule[1])
            else:
                product = [int(x) for x in product_rule.split(" ")]
                products.append(product)
        rules[int(rule_number)] = products

        index += 1

    return rules


if __name__ == "__main__":

    with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    rules = parse_rules(lines)

    print(f"Part 1: Answer: {part1(lines, rules)}")
    print(f"Part 2: Answer: {part2(lines)}")
