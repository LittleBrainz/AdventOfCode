# AdventOfCode/2023/day03/solution.py
#
# Day 3: Gear Ratios
#
# https://adventofcode.com/2023/day/3


symbols = {'*', '+', '%', '@', '=', '-', '/', '#', '$', '&'}


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> list[str]:
    rows = ['.' + row + '.' for row in text.split('\n')]
    row0 = '.' * len(rows[0])
    rows = [row0] + rows + [row0]
    return rows


def calc_part_1(rows: list[str]) -> int:
    part_sum = 0
    part_num = 0
    near = False
    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[r]) - 1):
            char = rows[r][c]
            if char.isdigit():
                part_num = part_num * 10 + int(char)
                near = near or check_near(rows, r, c)
            else:
                if near:
                    part_sum += part_num
                part_num = 0
                near = False
    return part_sum


def calc_part_2(rows: list[str]) -> int:
    return 0


def check_near(rows: list[str], r: int, c: int) -> bool:
    for rn in [r - 1, r, r + 1]:
        for cn in [c - 1, c, c + 1]:
            if rows[rn][cn] in symbols:
                return True
    return False


if __name__ == '__main__':
    # main('example.txt')
    main('input.txt')
