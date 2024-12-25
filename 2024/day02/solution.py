# AdventOfCode/2024/day02/solution.py
#
# Day 2: Red-Nosed Reports
#
# https://adventofcode.com/2024/day/2


from dataclasses import dataclass


@dataclass
class Report:
    levels: list[int]

@dataclass
class Data:
    reports: list[Report]


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> Data:
    reports = [parse_line(line) for line in text.split('\n')]
    return Data(reports)


def parse_line(line: str) -> Report:
    levels = [int(level) for level in line.split(' ')]
    return Report(levels)


def calc_part_1(data: Data) -> int:
    safes = [calc_safe(report.levels) for report in data.reports]
    return sum(safes)


def calc_part_2(data: Data) -> int:
    safes = [calc_safeish(report.levels) for report in data.reports]
    return sum(safes)


def calc_safe(levels: list[int]) -> int:
    pos = False
    neg = False
    for (l0, l1) in zip(levels[:-1], levels[1:]):
        if l0 < l1:
            if l1 - l0 > 3 or neg:
                return 0
            pos = True
        if l0 == l1:
            return 0
        if l0 > l1:
            if l0 - l1 > 3 or pos:
                return 0
            neg = True
    return 1


def calc_safeish(levels: list[int]) -> int:
    if calc_safe(levels) == 1:
        return 1
    for i in range(len(levels)):
        levelsx = levels[:i] + levels[i+1:]
        if calc_safe(levelsx) == 1:
            return 1
    return 0


if __name__ == '__main__':
    main('example.txt')
    main('input.txt')
