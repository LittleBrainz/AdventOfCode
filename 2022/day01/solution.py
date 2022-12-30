# AdventOfCode/2022/day01/solution.py
#
# Day 1: Calorie Counting
#
# https://adventofcode.com/2022/day/1


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[int]:
    return [parse_group(group_text) for group_text in input_text.split("\n\n")]


def parse_group(group_text: str) -> int:
    return sum(int(line_text) for line_text in group_text.split("\n"))


def calc_part1(calories_list: list[int]) -> int:
    return max(calories_list)


def calc_part2(calories_list: list[int]) -> int:
    return sum(sorted(calories_list, reverse=True)[0:3])


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
