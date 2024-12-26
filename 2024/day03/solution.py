# AdventOfCode/2024/day03/solution.py
#
# Day 3: Mull It Over
#
# https://adventofcode.com/2024/day/3


import re


mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

do_pattern = r'do\(\)(.*?)don\'t\(\)'


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> str:
    lines = [line for line in text.split('\n')]
    return ''.join(lines)


def calc_part_1(data: str) -> int:
    matches = re.findall(mul_pattern, data)
    muls = [int(match[0]) * int(match[1]) for match in matches]
    return sum(muls)


def calc_part_2(data: str) -> int:
    matches = re.findall(do_pattern, 'do()' + data + 'don\'t()')
    return calc_part_1(''.join(matches))


if __name__ == '__main__':
    main('example1.txt')
    main('example2.txt')
    main('input.txt')
