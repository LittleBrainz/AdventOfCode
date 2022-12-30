# AdventOfCode/2022/day11/solution.py
#
# Day 11: Monkey in the Middle
#
# https://adventofcode.com/2022/day/11


from copy import deepcopy

from dataclasses import dataclass


@dataclass
class Monkey:
    id:      int
    opcode:  list[str]
    div_by:  int
    if_T:    int
    if_F:    int
    inspect: int
    items:   list[int]


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[Monkey]:
    return [parse_group(group_text, id) 
            for (id, group_text) in enumerate(input_text.split("\n\n"))]


def parse_group(group_text: str, id: int) -> Monkey:
    _, items_t, opcode_t, div_by_t, if_true_t, if_false_t = group_text.split("\n")
    items    = list(map(int, items_t[18:].split(", ")))
    opcode   = opcode_t[23:].split(" ")
    div_by   = int(div_by_t[21:])
    if_true  = int(if_true_t[29:])
    if_false = int(if_false_t[30:])
    return Monkey(id, opcode, div_by, if_true, if_false, 0, items)


def calc_part1(monkey_list: list[Monkey]) -> int:
    return do_rounds(deepcopy(monkey_list), 20)


def calc_part2(monkey_list: list[Monkey]) -> int:
    return do_rounds(deepcopy(monkey_list), 200)


def do_rounds(monkey_list: list[Monkey], rounds: int) -> int:
    for round in range(rounds):
        for mk in monkey_list:
            for worry in mk.items:
                mk.inspect += 1
                worry = calc_worry(worry, mk)
                mk2 = monkey_list[mk.if_T if (worry % mk.div_by == 0) else mk.if_F]
                worry = fix_worry(worry, mk2)
                mk2.items.append(worry)
            mk.items = []
        # print_monkey_list_items(monkey_list, round + 1)
        # if round % 10 == 0:
        #     print(end=".", flush=True)
    print_monkey_list_inspect(monkey_list, rounds)
    (mi1, mi2) = sorted([monkey.inspect for monkey in monkey_list], reverse=True)[:2]
    return mi1 * mi2


def calc_worry(worry: int, mk: Monkey) -> int:
    (op, arg_t) = mk.opcode
    arg = worry if arg_t == "old" else int(arg_t)
    return (worry + arg, worry * arg)["+*".index(op)] // 3


def fix_worry(worry: int, mk2: Monkey) -> int:
    (op, arg_t) = mk2.opcode
    arg = worry if arg_t == "old" else int(arg_t)
    if op == "*":
        remainder = (worry * arg // 3) % mk2.div_by
        # do something magical to reduce an out-of-control worry
        worry = worry
    return worry


def print_monkey_list(monkey_list: list[Monkey]) -> None:
    for m in range(len(monkey_list)):
        mk = monkey_list[m]
        items = str(mk.items)[1:-1]
        print(f"{m} - id:{mk.id:2d}  op: {mk.opcode[0]:1} {mk.opcode[1]:3}  " + 
            f"div: {mk.div_by:2d}  T: {mk.if_T:1d}  F: {mk.if_F:1d}  items: {items}")
    print()


def print_monkey_list_items(monkey_list: list[Monkey], round: int) -> None:
    print(f"After round {round}")
    for m in range(len(monkey_list)):
        items = str(monkey_list[m].items)[1:-1]
        print(f"  Monkey {m}: {items}")
    print()


def print_monkey_list_inspect(monkey_list: list[Monkey], rounds: int) -> None:
    print(f"After round {rounds}")
    for m in range(len(monkey_list)):
        print(f"  Monkey {m} inspected items {monkey_list[m].inspect}")
    print()


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
