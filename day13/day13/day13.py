# AOC 2020 Day 13

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2020" / "day13" / "day13"


def part1(earliest, busses):
    nearest = max(busses)
    first_bus = 0

    for bus in busses:
        next_time = (int(earliest / bus) + 1) * bus
        if next_time - earliest < nearest:
            nearest = next_time - earliest
            first_bus = bus

    return first_bus * nearest


def part2(bus_times):

    current_time = 99999999999984
    done = False

    while not done:
        current_time += bus_times[0][0]
        fit = 0
        for bus_time in bus_times:
            if not (current_time + bus_time[1]) % bus_time[0]:
                fit += 1
            else:
                break

        done = (fit == len(bus_times))
        
    return current_time

        
def parse_line(line):
    busses = []
    for bus in line.split(","):
        if bus != "x":
            busses.append(int(bus))

    return busses

def parse_times(bus_line):
    bus_times = []
    time = 0

    for bus in bus_line.split(","):
        if bus != "x":
            bus_times.append((int(bus), time))
        time += 1

    return bus_times


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        earliest = int(f.readline())
        bus_line = f.readline().strip()
        busses = parse_line(bus_line)
        bus_times = parse_times(bus_line)

    print(f"Part 1: Answer: {part1(earliest, busses)}")
    print(f"Part 2: Answer: {part2(bus_times)}")
