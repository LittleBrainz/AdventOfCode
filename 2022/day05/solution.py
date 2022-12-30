# AdventOfCode/2022/day05/solution.py
#
# Day 5: Supply Stacks
#
# https://adventofcode.com/2022/day/5


from copy import deepcopy

from dataclasses import dataclass


@dataclass
class Move:
    qty: int
    s0:  int
    s1:  int

@dataclass
class StacksMoves:
    stacks: list[list[str]]
    moves:  list[Move]


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> StacksMoves:
    stacks_text, moves_text = input_text.split("\n\n")
    stacks = parse_stacks(stacks_text)
    moves = parse_moves(moves_text)
    return StacksMoves(stacks, moves)


def parse_stacks(stacks_text: str) -> list[list[str]]:
    layers = stacks_text.split("\n")[-2::-1]
    count = (len(layers[0]) + 1) // 4
    stacks = [[] for _ in range(count)]
    for layer in layers:
        for s in range(count):
            crate = layer[1 + 4 * s]
            if crate != " ":
                stacks[s].append(crate)
    return stacks


def parse_moves(moves_text: str) -> list[Move]:
    return [parse_move(move_text) for move_text in moves_text.split("\n")]


def parse_move(move_text: str) -> Move:
    _, qty_t, _, s0_t, _, s1_t = move_text.split(" ")
    return Move(int(qty_t), int(s0_t) - 1, int(s1_t) - 1)


def calc_part1(stacks_moves: StacksMoves) -> str:
    return move_crates(stacks_moves, order=-1)


def calc_part2(stacks_moves: StacksMoves) -> str:
    return move_crates(stacks_moves, order=1)


def move_crates(stacks_moves: StacksMoves, order: int) -> str:
    stacks = deepcopy(stacks_moves.stacks)
    for m in stacks_moves.moves:
        stacks[m.s1] += stacks[m.s0][-m.qty:][::order]
        stacks[m.s0]  = stacks[m.s0][:-m.qty]
    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
