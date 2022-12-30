# AdventOfCode/2022/day09/solution.py
#
# Day 9: Rope Bridge
#
# https://adventofcode.com/2022/day/9


from dataclasses import dataclass


@dataclass
class Vec:
    x: int
    y: int

@dataclass
class Move:
    uvec: Vec
    mag:  int


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[Move]:
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text: str) -> Move:
    uvec_t, mag_t = line_text.split(" ")
    uvec = {"R": Vec(1,0), "U": Vec(0,1), "L": Vec(-1,0), "D": Vec(0,-1)}[uvec_t]
    return Move(uvec, int(mag_t))


def calc_part1(move_list: list[Move]) -> int:
    H_loc = Vec(0, 0)
    T_loc = Vec(0, 0)
    T_path = {tup(T_loc)}
    for move in move_list:
        for _ in range(move.mag):
            H_loc = add(H_loc, move.uvec)
            if dist(H_loc, T_loc) > 1:
                T_loc = add(T_loc, nudge(H_loc, T_loc))
            T_path.add(tup(T_loc))
    return len(T_path)


def calc_part2(move_list: list[Move]) -> int:
    K_locs = [Vec(0, 0) for _ in range(10)]
    K9_path = {tup(K_locs[9])}
    for move in move_list:
        for _ in range(move.mag):
            K_locs[0] = add(K_locs[0], move.uvec)
            for k in range(1, 10):
                if dist(K_locs[k-1], K_locs[k]) <= 1:
                    break
                K_locs[k] = add(K_locs[k], nudge(K_locs[k-1], K_locs[k]))
            K9_path.add(tup(K_locs[9]))
    return len(K9_path)


def dist(loc1: Vec, loc0: Vec) -> int:
    vec = sub(loc1, loc0)
    return max(abs(vec.x), abs(vec.y))


def nudge(loc1: Vec, loc0: Vec) -> Vec:
    vec = sub(loc1, loc0)
    return Vec(sign(vec.x), sign(vec.y))


def add(loc: Vec, vec: Vec) -> Vec:
    return Vec(loc.x + vec.x, loc.y + vec.y)


def sub(loc1: Vec, loc0: Vec) -> Vec:
    return Vec(loc1.x - loc0.x, loc1.y - loc0.y)


def sign(num: int) -> int:
    return 0 if num == 0 else num // abs(num)


def tup(vec: Vec) -> tuple[int, int]:
    return (vec.x, vec.y)


if __name__ == "__main__":
    main("example1.txt")
    main("example2.txt")
    main("input.txt")
