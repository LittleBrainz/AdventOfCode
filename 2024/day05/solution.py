# AdventOfCode/2024/day03/solution.py
#
# Day 5: Print Queue
#
# https://adventofcode.com/2024/day/5


from dataclasses import dataclass


@dataclass
class Data:
    lines: list[str]
    ym: int
    xm: int


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> str:
    lines = [line for line in text.split('\n')]
    return Data(lines, len(lines) - 1, len(lines[0]) - 1)


def calc_part_1(d: Data) -> int:
    return 0


def calc_part_2(d: Data) -> int:
    return 0


if __name__ == '__main__':
    main('example.txt')
    # main('input.txt')
