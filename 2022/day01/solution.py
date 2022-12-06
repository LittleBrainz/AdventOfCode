# AdventOfCode/2022/day01/solution.py
#
# Day 1: Calorie Counting
#
# https://adventofcode.com/2022/day/1


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().strip()
    input_list = parse_text(input_text)
    result1 = part1(input_list)
    result2 = part2(input_list)
    print(result1, result2)


def parse_text(input_text):
    return [parse_group(group_text)
            for group_text in input_text.split("\n\n")]


def parse_group(group_text):
    return sum(int(line) for line in group_text.split("\n"))


def part1(input_list):
    return max(input_list)


def part2(input_list):
    return sum(sorted(input_list, reverse=True)[0:3])


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
