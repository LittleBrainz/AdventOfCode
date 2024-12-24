# AdventOfCode/2024/day01/solution.py
#
# Day 1: Historian Hysteria
#
# https://adventofcode.com/2024/day/1


from collections import Counter


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> tuple[list[int], list[int]]:
    lines = text.split('\n')
    l_list = [int(line.split('   ')[0]) for line in lines]
    r_list = [int(line.split('   ')[1]) for line in lines]
    return (l_list, r_list)


def calc_part_1(data: tuple[list[int], list[int]]) -> int:
    (l_list, r_list) = data
    d_list = [abs(l - r) for l, r in zip(sorted(l_list), sorted(r_list))]
    return sum(d_list)


def calc_part_2(data: tuple[list[int], list[int]]) -> int:
    (l_list, r_list) = data
    r_dict = Counter(r_list)
    c_list = [l * r_dict.get(l, 0) for l in l_list]
    return sum(c_list)


if __name__ == '__main__':
    main('example.txt')
    main('input.txt')
