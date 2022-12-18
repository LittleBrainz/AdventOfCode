# AdventOfCode/2022/day05/solution.py
#
# Day 5: Supply Stacks
#
# https://adventofcode.com/2022/day/5


from copy import deepcopy


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text):
    stacks_text, moves_text = input_text.split("\n\n")
    stacks = parse_stacks(stacks_text)
    moves = parse_moves(moves_text)
    return {"stacks": stacks, "moves": moves}


def parse_stacks(stacks_text):
    layers = stacks_text.split("\n")[-2::-1]
    count = (len(layers[0]) + 1) // 4
    stacks = [[] for _ in range(count)]
    for layer in layers:
        for s in range(count):
            crate = layer[1 + 4 * s]
            if crate != " ":
                stacks[s].append(crate)
    return stacks


def parse_moves(moves_text):
    return [parse_move(move_text) for move_text in moves_text.split("\n")]


def parse_move(move_text):
    _, qty_t, _, s0_t, _, s1_t = move_text.split(" ")
    return (int(qty_t), int(s0_t) - 1, int(s1_t) - 1)


def calc_part1(input_data):
    return move_crates(input_data, order=-1)


def calc_part2(input_data):
    return move_crates(input_data, order=1)


def move_crates(input_data, order):
    stacks = deepcopy(input_data["stacks"])
    for qty, s0, s1 in input_data["moves"]:
        stacks[s1] += stacks[s0][-qty:][::order]
        stacks[s0]  = stacks[s0][:-qty]
    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
