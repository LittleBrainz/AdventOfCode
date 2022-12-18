# AdventOfCode/2022/day01/solution.py
#
# Day 1: Calorie Counting
#
# https://adventofcode.com/2022/day/1


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text):
    return [parse_group(group_text) for group_text in input_text.split("\n\n")]


def parse_group(group_text):
    return sum(int(line_text) for line_text in group_text.split("\n"))


def calc_part1(input_data):
    return max(input_data)


def calc_part2(input_data):
    return sum(sorted(input_data, reverse=True)[0:3])


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
