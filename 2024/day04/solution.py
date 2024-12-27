# AdventOfCode/2024/day03/solution.py
#
# Day 3: Mull It Over
#
# https://adventofcode.com/2024/day/3


from dataclasses import dataclass


@dataclass
class Data:
    lines: list[str]
    xm: int
    ym: int


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> str:
    lines = [line for line in text.split('\n')]
    return Data(lines, len(lines[0])-1, len(lines)-1)


def calc_part_1(data: Data) -> int:
    munges = [munge(data, xd, yd) for (xd, yd) in
        [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]]
    return 0


def calc_part_2(data: Data) -> int:
    return 0


def munge(data: Data, xd: int, yd: int) -> str:
    mag = data.rows + data.cols
    for m in range(-mag, mag):
        pass
    text = ''
    for row in range(data.rows):
        for col in range(data.cols):
            text += data.lines[row][col]
        text += ' '
    return text


def rrange(i0: int, i1: int) -> range:
    if i0 > i1:
        return range(i0, i1-1, -1)
    return range(i0, i1+1)


if __name__ == '__main__':
    main('example.txt')
    # main('input.txt')
