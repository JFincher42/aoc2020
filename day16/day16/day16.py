# AOC 2020 Day 16

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day16" / "day16"
invalid_tickets = set()


def part1(lines, known_fields):

    global invalid_tickets

    invalid_fields = 0
    invalid_ticket_lines = []

    # Build a set of valid numbers
    valid_fields = set()
    for _, field_set in known_fields.items():
        valid_fields |= field_set

    # Find where the nearby tickets start
    for index, line in enumerate(lines):
        if line.strip() == "nearby tickets:":
            break

    # Process each ticket
    index += 1
    while index < len(lines):
        for ticket_field in [int(x) for x in lines[index].split(",")]:
            if ticket_field not in valid_fields:
                invalid_fields += ticket_field
                invalid_ticket_lines.append(index)

        index += 1

    invalid_tickets = set(invalid_ticket_lines)

    return invalid_fields


def check_value(field_value, class_names, fields):

    valid_class_names = []

    for ticket_class in class_names:
        if field_value in fields[ticket_class]:
            valid_class_names.append(ticket_class)

    return set(valid_class_names)

def reduce_classes(valid_classes):

    classes_seen = set()

    while len(classes_seen) < len(valid_classes):

        # Find the next item with a single class
        for i, class_set in enumerate(valid_classes):
            if len(class_set) == 1:
                # Have we see it already?
                if class_set & classes_seen:
                    continue

                # Add it to the list
                classes_seen |= class_set

                # Remove it from the rest of the list
                for classes in valid_classes:
                    if len(classes) > 1:
                        classes -= class_set

    return valid_classes


def part2(lines, fields):

    global invalid_tickets

    # List of valid classes
    ticket_classes = set([ticket_class for ticket_class in fields.keys()])
    valid_ticket_classes = [ticket_classes.copy() for _ in range(len(ticket_classes))]

    # Find where my ticket is
    for line_index, line in enumerate(lines):
        if line.strip() == "your ticket:":
            break

    my_ticket = [int(x) for x in lines[line_index + 1].split(",")]

    # Find where the nearby tickets start
    for line_index, line in enumerate(lines):
        if line.strip() == "nearby tickets:":
            break

    # Process each ticket
    line_index += 1
    while line_index < len(lines):
        if line_index in invalid_tickets:
            line_index += 1
            continue

        current_ticket_field_value_list = [int(x) for x in lines[line_index].split(",")]
        for current_ticket_field_index, current_ticket_field_value in enumerate(
            current_ticket_field_value_list
        ):
            valid_ticket_classes[current_ticket_field_index] &= check_value(
                current_ticket_field_value,
                valid_ticket_classes[current_ticket_field_index],
                fields,
            )

        line_index += 1

    valid_ticket_classes = reduce_classes(valid_ticket_classes)

    answer = 1
    for line_index, field_name in enumerate(valid_ticket_classes):
        if field_name.pop()[:9] == "departure":
            answer *= my_ticket[line_index]

    return answer


def parse_fields(lines):

    fields = {}

    for line in lines:
        if not line:
            return fields

        field_name, field_ranges = line.split(": ")
        field_range_list = []
        field_range_set = set()
        for field_range in field_ranges.split(" or "):
            field_top, field_bottom = field_range.split("-")
            field_range_list = [
                field for field in range(int(field_top), int(field_bottom) + 1)
            ]
            field_range_set |= set(field_range_list)

        fields[field_name.strip()] = field_range_set

    return fields


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    fields = parse_fields(lines)

    print(f"Part 1: Answer: {part1(lines, fields)}")
    print(f"Part 2: Answer: {part2(lines, fields)}")
