# AdventOfCode/2022/day03/solution.py
#
# Day 3: Rucksack Reorganization
#
# https://adventofcode.com/2022/day/3


from dataclasses import dataclass


@dataclass
class Contents:
    c1: set[str]
    c2: set[str]


PRIORITY = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[Contents]:
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text: str) -> Contents:
    mid = len(line_text) // 2
    c1 = set(line_text[:mid])
    c2 = set(line_text[mid:])
    return Contents(c1, c2)


def calc_part1(contents_list: list[Contents]) -> int:
    return sum(calc_priority1(contents) for contents in contents_list)


def calc_part2(contents_list: list[Contents]) -> int:
    return sum(calc_priority2(contents_list[i:i+3])
            for i in range(0, len(contents_list), 3))


def calc_priority1(contents: Contents) -> int:
    return priority(list(contents.c1.intersection(contents.c2))[0])


def calc_priority2(contents_list: list[Contents]) -> int:
    items = set(PRIORITY)
    for contents in contents_list:
        items = items.intersection(contents.c1.union(contents.c2))
    return priority(list(items)[0])


def priority(item: str) -> int:
    return PRIORITY.index(item)


def priority_alt(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    return ord(item) - 64 + 26


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
