# AdventOfCode/2022/day09/solution.py
#
# Day 9: Rope Bridge
#
# https://adventofcode.com/2022/day/9


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text: str) -> list[tuple]:
    return [parse_line(input_line) for input_line in input_text.split("\n")]


def parse_line(input_line: str) -> tuple:
    uvec_t, mag_t = input_line.split(" ")
    uvec = {"R": (1,0), "U": (0,1), "L": (-1,0), "D": (0,-1)}[uvec_t]
    return (uvec, int(mag_t))


def calc_part1(input_data: list[tuple]):
    H_loc = (0,0)
    T_loc = (0,0)
    T_path = {T_loc}
    for (uvec, mag) in input_data:
        for _ in range(mag):
            H_loc = add(H_loc, uvec)
            if dist(H_loc, T_loc) > 1:
                T_loc = add(T_loc, move(H_loc, T_loc))
            T_path.add(T_loc)
    return len(T_path)


def calc_part2(input_data: list[tuple]):
    K_locs = [(0,0) for _ in range(10)]
    K9_path = {K_locs[9]}
    for (uvec, mag) in input_data:
        for _ in range(mag):
            K_locs[0] = add(K_locs[0], uvec)
            for k in range(1, 10):
                if dist(K_locs[k], K_locs[k-1]) <= 1:
                    break
                K_locs[k] = add(K_locs[k], move(K_locs[k-1], K_locs[k]))
            K9_path.add(K_locs[9])
    return len(K9_path)


def add(loc: tuple[int, int], vec: tuple[int, int]) -> tuple[int, int]:
    return (loc[0] + vec[0], loc[1] + vec[1])


def sub(loc1: tuple[int, int], loc0: tuple[int, int]) -> tuple[int, int]:
    return (loc1[0] - loc0[0], loc1[1] - loc0[1])


def dist(loc1: tuple[int, int], loc0: tuple[int, int]) -> int:
    vec = sub(loc1, loc0)
    return max(abs(vec[0]), abs(vec[1]))


def move(loc1: tuple[int, int], loc0: tuple[int, int]) -> tuple[int, int]:
    vec = sub(loc1, loc0)
    return (sign(vec[0]), sign(vec[1]))


def sign(num: int) -> int:
    return 0 if num == 0 else num // abs(num)


if __name__ == "__main__":
    main("example1.txt")
    main("example2.txt")
    main("input.txt")
