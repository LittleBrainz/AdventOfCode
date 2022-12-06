# AdventOfCode/2022/day02/solution.py
#
# Day 2: Rock Paper Scissors
#
# https://adventofcode.com/2022/day/2


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().strip()
    input_list = parse_text(input_text)
    result1 = part1(input_list)
    result2 = part2(input_list)
    print(result1, result2)


def parse_text(input_text):
    return [parse_line(input_line)
            for input_line in input_text.split("\n")]


def parse_line(input_line):
    op_t, me_t = input_line.split()
    op = "ABC".index(op_t)
    me = "XYZ".index(me_t)
    return (op, me)


def part1(input_list):
    return sum(calc_score1(op, me) for (op, me) in input_list)


def part2(input_list):
    return sum(calc_score2(op, me) for (op, me) in input_list)


def calc_score1(op, me):
    outcome = ((me - op + 1) % 3) * 3
    return (me + 1) + outcome


def calc_score2(op, me):
    me2 = (op + (me - 1)) % 3
    return calc_score1(op, me2)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
