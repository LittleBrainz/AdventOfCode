# AdventOfCode/2024/day01/solution.py
#
# Day 1: Historian Hysteria
#
# https://adventofcode.com/2024/day/1


from collections import Counter
from dataclasses import dataclass


@dataclass
class Data:
    l_list: list[int]
    r_list: list[int]


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> Data:
    lines = text.split('\n')
    l_list = [int(line.split('   ')[0]) for line in lines]
    r_list = [int(line.split('   ')[1]) for line in lines]
    return Data(l_list, r_list)


def calc_part_1(data: Data) -> int:
    d_list = [abs(l - r) for l, r in zip(sorted(data.l_list), sorted(data.r_list))]
    return sum(d_list)


def calc_part_2(data: Data) -> int:
    r_dict = Counter(data.r_list)
    c_list = [l * r_dict.get(l, 0) for l in data.l_list]
    return sum(c_list)


if __name__ == '__main__':
    main('example.txt')
    main('input.txt')
