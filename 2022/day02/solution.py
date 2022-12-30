# AdventOfCode/2022/day02/solution.py
#
# Day 2: Rock Paper Scissors
#
# https://adventofcode.com/2022/day/2


from dataclasses import dataclass


@dataclass
class Strategy:
    op: int
    me: int


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[Strategy]:
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text: str) -> Strategy:
    op_t, me_t = line_text.split()
    op = "ABC".index(op_t)
    me = "XYZ".index(me_t)
    return Strategy(op, me)


def calc_part1(strategy_list: list[Strategy]) -> int:
    return sum(calc_score1(strategy) for strategy in strategy_list)


def calc_part2(strategy_list: list[Strategy]) -> int:
    return sum(calc_score2(strategy) for strategy in strategy_list)


def calc_score1(s: Strategy) -> int:
    outcome = ((s.me - s.op + 1) % 3) * 3
    return (s.me + 1) + outcome


def calc_score2(s: Strategy) -> int:
    me2 = (s.op + (s.me - 1)) % 3
    return calc_score1(Strategy(s.op, me2))


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
