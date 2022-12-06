# AdventOfCode/2022/day03/solution.py
#
# Day 3: Rucksack Reorganization
#
# https://adventofcode.com/2022/day/3


PRIORITY = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().strip()
    input_list = parse_text(input_text)
    result1 = part1(input_list)
    result2 = part2(input_list)
    print(result1, result2)


def parse_text(input_text):
    return [parse_line(input_line)
            for input_line in input_text.split("\n")]


def parse_line(input_line):
    mid = len(input_line) // 2
    c1 = set(input_line[:mid])
    c2 = set(input_line[mid:])
    return (c1, c2)


def part1(input_list):
    return sum(calc_priority1(c1, c2) for (c1, c2) in input_list)


def part2(input_list):
    return sum(calc_priority2(input_list[i:i+3])
            for i in range(0, len(input_list), 3))


def calc_priority1(c1, c2):
    return priority(list(c1.intersection(c2))[0])


def calc_priority2(group_list):
    items = set(PRIORITY)
    for (c1, c2) in group_list:
        items = items.intersection(c1.union(c2))
    return priority(list(items)[0])


def priorityXXX(item):
    return PRIORITY.index(item)


def priority(item):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 64 + 26


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
