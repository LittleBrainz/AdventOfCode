# AdventOfCode/2022/day10/solution.py
#
# Day 10: Cathode-Ray Tube
#
# https://adventofcode.com/2022/day/10


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    print(input_data)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text: str) -> list[tuple]:
    return [parse_line(input_line) for input_line in input_text.split("\n")]


def parse_line(input_line: str) -> tuple:
    tokens = input_line.split(" ")
    opc = tokens[0]
    arg = int(tokens[1]) if len(tokens) == 2 else 0
    return (opc, arg)


def calc_part1(input_data: list[tuple]):
    return


def calc_part2(input_data: list[tuple]):
    return


if __name__ == "__main__":
    main("example1.txt")
    # main("example2.txt")
    # main("input.txt")
