# AOC 2020 Day 21

import pathlib
from pprint import pprint

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day21"


def process_lines(lines):
    allergens = dict()
    for line in lines:
        ingredients = set()
        processing_ingredients = True
        for word in line.split():
            if word == "(contains":
                processing_ingredients = False
            elif processing_ingredients:
                ingredients.add(word)
            else:
                # get rid of the trailing comma or paren
                word = word[:-1]
                if word not in allergens.keys():
                    allergens[word] = []
                allergens[word].append(ingredients)

    return allergens


def intersect(ingredient_sets):
    intersection = ingredient_sets[0]
    for i in range(1, len(ingredient_sets)):
        intersection = intersection.intersection(ingredient_sets[i])
    return intersection


def simplify(allergens):
    simplified_allergens = dict()
    for allergen, ingredient_sets in allergens.items():
        if len(ingredient_sets) > 1:
            common_ingredients = intersect(ingredient_sets)
        else:
            common_ingredients = ingredient_sets[0]
        simplified_allergens[allergen] = common_ingredients
    return simplified_allergens


def has_multiple_ingredients(allergens):
    multiple_ingredients = False
    for _, ingredient_set in allergens:
        multiple_ingredients = multiple_ingredients or len(ingredient_set) > 1
    return multiple_ingredients


def part1(allergens):
    simple_allergens = simplify(allergens)
    allergens = list(simple_allergens.keys())
    for allergen in allergens:
        if len(allergens[allergen]) == 1:
            pass


def part2():
    pass


if __name__ == "__main__":

    with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    allergens = process_lines(lines)
    # pprint(allergens)

    print(f"Part 1: Answer: {part1(allergens)}")
    print(f"Part 2: Answer: {part2()}")
