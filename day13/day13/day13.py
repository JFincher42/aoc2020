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


    # current_time = 100000000000080
    current_time = 0
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
        
def part2_redux(bus_times):

    # The idea here is to combine everything pairwise
    # Start with the first one
    # Combine it with the next one
    # Put that answer into current_bus_time
    # Then combine it with the next one
    
    current_bus_time = bus_times[0]
    timestamp = 0

    for bus_time in bus_times[1:]:
        # Find the next time that work for current_bus_time and this one
        while ((timestamp + bus_time[1]) % bus_time[0]):
            timestamp += current_bus_time[0]
        current_bus_time = (current_bus_time[0] * bus_time[0], timestamp)

    return timestamp

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
    # print(f"Part 2: Answer: {part2(bus_times)}")
    print(f"Part 2 Redux: Answer: {part2_redux(bus_times)}")
