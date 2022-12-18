# AdventOfCode/2022/day04/solution.py
#
# Day 4: Camp Cleanup
#
# https://adventofcode.com/2022/day/4


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
    e1_t, e2_t = line_text.split(",")
    e1f_t, e1t_t = e1_t.split("-")
    e2f_t, e2t_t = e2_t.split("-")
    return (int(e1f_t), int(e1t_t)), (int(e2f_t), int(e2t_t))


def calc_part1(input_data):
    return sum(contains(e1, e2) for (e1, e2) in input_data)


def calc_part2(input_data):
    return sum(overlaps(e1, e2) for (e1, e2) in input_data)


def overlaps(e1, e2):
    ol = overlap(e1, e2)
    return 1 if width(ol) > 0 else 0


def contains(e1, e2):
    ol = overlap(e1, e2)
    return 1 if width(ol) >= width(e1) or width(ol) >= width(e2) else 0


def overlap(e1, e2):
    return max(e1[0], e2[0]), min(e1[1], e2[1])


def width(e):
    return max(0, e[1] - e[0] + 1)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
