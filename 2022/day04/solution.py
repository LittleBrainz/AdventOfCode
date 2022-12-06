# AdventOfCode/2022/day04/solution.py
#
# Day 4: Camp Cleanup
#
# https://adventofcode.com/2022/day/4


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
    e1_t, e2_t = input_line.split(",")
    e1f_t, e1t_t = e1_t.split("-")
    e2f_t, e2t_t = e2_t.split("-")
    return (int(e1f_t), int(e1t_t)), (int(e2f_t), int(e2t_t))


def part1(input_list):
    return sum(is_contained(e1, e2) for e1, e2 in input_list)


def part2(input_list):
    return sum(is_overlapped(e1, e2) for e1, e2 in input_list)


def is_overlapped(e1, e2):
    ol = calc_overlap(e1, e2)
    return 1 if width(ol) > 0 else 0


def is_contained(e1, e2):
    ol = calc_overlap(e1, e2)
    return 1 if width(ol) >= width(e1) or width(ol) >= width(e2) else 0


def calc_overlap(e1, e2):
    return max(e1[0], e2[0]), min(e1[1], e2[1])


def width(e):
    return max(0, e[1] - e[0] + 1)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
