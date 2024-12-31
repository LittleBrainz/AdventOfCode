# AdventOfCode/2024/day03/solution.py
#
# Day 3: Mull It Over
#
# https://adventofcode.com/2024/day/3


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
    l_r = [[d.lines[y][x]
            for y in rrange(0, d.ym)]
                for x in rrange(0, d.xm)]
    t_b = [[d.lines[y][x]
            for x in rrange(0, d.xm)]
                for y in rrange(0, d.ym)]
    dup = [[d.lines[y-x][x]
            for x in rrange(max(0, y - d.ym), min(d.xm, y))]
                for y in rrange(0, d.ym + d.xm)]
    ddn = [[d.lines[y+x][x]
            for x in rrange(max(0, -y), min(d.xm, d.ym - y))]
                for y in rrange(-d.xm, d.ym)]
    slices = ' '.join(''.join(cs) for cs in l_r + t_b + dup + ddn)
    return (slices + ' ' + slices[::-1]).count('XMAS')


def calc_part_2(d: Data) -> int:
    count = 0
    for y in rrange(1, d.ym - 1):
        for x in rrange(1, d.xm - 1):
            if d.lines[y][x] != 'A':
                continue
            msms = d.lines[y-1][x-1] + d.lines[y+1][x+1] + d.lines[y-1][x+1] + d.lines[y+1][x-1]
            if msms not in 'MSMS MSSM SMMS SMSM':
                continue
            count += 1
    return count


def rrange(i0: int, i1: int) -> range:
    if i0 > i1:
        return range(i0, i1-1, -1)
    return range(i0, i1+1)


if __name__ == '__main__':
    main('example.txt')
    main('input.txt')
