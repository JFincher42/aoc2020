# AOC 2020 Day 19

import pathlib
import re

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day19" / "day19"


def convertToRegex(rule, rulesDict):
    returnRule = ""
    if rule in ["a", "b"]:
        returnRule = rule
    else:
        returnRule = returnRule + "("
        if rule.find("|") > 0:
            subRules = rule.split(" | ")
            for sub in subRules:
                nums = sub.split(" ")
                for num in nums:
                    # print(rulesDict[int(num)])
                    returnRule = returnRule + convertToRegex(
                        rulesDict[int(num)], rulesDict
                    )
                returnRule = returnRule + "|"
            returnRule = returnRule[0 : len(returnRule) - 1]  # get rid of last |
        else:  # there is no or operator
            nums = rule.split(" ")
            for num in nums:
                # print(rulesDict[int(num)])
                returnRule = returnRule + convertToRegex(rulesDict[int(num)], rulesDict)
        returnRule = returnRule + ")"
    return returnRule


def convert_rules(line_rules):
    rules = {}
    for rule_num, rule in line_rules.items():
        converted_rule = convertToRegex(rule, line_rules)
        if converted_rule[0] == "(":
            converted_rule = converted_rule[1:-1]
        rules[rule_num] = converted_rule

    return rules


def part1(lines, rules):

    rule = "^" + rules[0] + "$"
    return sum(1 for line in lines if re.match(rule, line))


def part2(lines, rules):

    print(f"Rule 8: {rules[8]}")
    print(f"Rule 11: {rules[11]}")

    rules[8] = "" + rules[8] + "+"
    rules[11] = "" + rules[42] + "*" + rules[31] + "*"

    # print(f"New Rule 8: {rules[8]}")
    # print(f"New Rule 11: {rules[11]}")

    # rules = convert_rules(parse_rules(rule_lines))

    # return -1
    rule = "^" + rules[0] + "$"
    return sum(1 for line in lines if re.match(rule, line))


def parse_rules(lines):

    rules = {}

    for line in lines:

        rule_number, production_string = line.split(": ")

        # If this is an end state, it will be "a" or "b"
        # So we just need to grab that
        if '"' in production_string:
            production_string = production_string[1]

        rules[int(rule_number)] = production_string

        # index += 1

    return rules


if __name__ == "__main__":

    with open(root_path / "sample2", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    rule_lines = [x for x in lines if len(x) > 0 and ":" in x]
    message_lines = [x for x in lines if len(x) > 0 and x[0] in ["a", "b"]]

    # Find the first real line
    # index = 0
    # while lines[index]:
    #     index += 1
    # index += 1

    print(f"Part 1: Answer: {part1(message_lines, convert_rules(parse_rules(rule_lines)))}")

    p2rules = parse_rules(rule_lines)
    # p2rules[8] = "42 | 42 8"
    # p2rules[11] = "42 31 | 42 11 31"

    print(f"Part 2: Answer: {part2(message_lines,convert_rules(p2rules))}")
