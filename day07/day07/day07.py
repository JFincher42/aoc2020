# AOC 2020 Day 7

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day07" / "day07"


def part1(rules):
    bags = 0
    bag_to_find = "shiny gold"

    for bag_color, contents in rules.items():
        # First, we we looking at our bag color?
        if bag_color != bag_to_find:

            # Add the current color to our search list
            bags_to_search = [bag_color]
            # Which bags have we already searched
            searched_bags = set()
            searched_bags.add(bag_color)

            for search_item in bags_to_search:
                search_contents = rules[search_item]
                for content_info in search_contents:
                    if content_info[1] not in searched_bags:
                        bags_to_search.append(content_info[1])
                        searched_bags.add(content_info[1])
                # bags_to_search.remove(search_item)
                if bag_to_find in searched_bags:
                    bags += 1
                    break

    return bags


def part2(rules):
    bags = 0
    bag_to_find = "shiny gold"

    bags_to_add = rules[bag_to_find]
    for search_item in bags_to_add:
        for i in range(search_item[0]):
            bags_to_add.extend(rules[search_item[1]])

    for contents in bags_to_add:
        bags += contents[0]

    return bags




def parse_rules(lines):
    """Parse the rules from a file.

    Rules consist of a bag color and a set of contents.
    The bag color is the key to the dictionary.
    The contents are kept in a list of tuples.
    Each tuple consists of a count and a bag color.

    Args:
        lines (list): lines containing plaintext rules

    Returns:
        dict: a dictionary of rules
    """
    rules = {}
    for line in lines:

        # First, split on the word " contains "

        rule_parts = line.split(" contain ")

        # The bag is the first part - just need to drop the final ' bags'
        bag = rule_parts[0][:-5]

        # Now we process the contents
        bag_contents = []
        for content_part in rule_parts[1].split(", "):
            # Are there other bags?
            if content_part == "no other bags.":
                break

            # Remove the final bags
            if content_part[-1] == ".":
                content_part = content_part[:-5].strip()
            else:
                content_part = content_part[:-4].strip()

            # Get the count and which bag
            content_count = int(content_part[0:1])
            content_color = content_part[2:]

            # Add this as a tuple to the bag_contents
            bag_contents.append((content_count, content_color))

        # Add this as an entry in the dictionary
        rules[bag] = bag_contents
    
    return rules


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    rules = parse_rules(lines)

    print(f"Part 1: Bags: {part1(rules)}")
    print(f"Part 2: Answer Count: {part2(rules)}")
