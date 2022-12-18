# AdventOfCode/2022/day02/solution.py
#
# Day 2: Rock Paper Scissors
#
# https://adventofcode.com/2022/day/2


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text):
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text):
    op_t, me_t = line_text.split()
    op = "ABC".index(op_t)
    me = "XYZ".index(me_t)
    return (op, me)


def calc_part1(input_data):
    return sum(calc_score1(op, me) for (op, me) in input_data)


def calc_part2(input_data):
    return sum(calc_score2(op, me) for (op, me) in input_data)


def calc_score1(op, me):
    outcome = ((me - op + 1) % 3) * 3
    return (me + 1) + outcome


def calc_score2(op, me):
    me2 = (op + (me - 1)) % 3
    return calc_score1(op, me2)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
