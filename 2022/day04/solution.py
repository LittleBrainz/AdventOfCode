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
    s1_t, s2_t = line_text.split(",")
    s1b_t, s1e_t = s1_t.split("-")
    s2b_t, s2e_t = s2_t.split("-")
    return (int(s1b_t), int(s1e_t)), (int(s2b_t), int(s2e_t))


def calc_part1(input_data):
    return sum(contains(s1, s2) for (s1, s2) in input_data)


def calc_part2(input_data):
    return sum(overlaps(s1, s2) for (s1, s2) in input_data)


def overlaps(s1, s2):
    ol = overlap(s1, s2)
    return 1 if width(ol) > 0 else 0


def contains(s1, s2):
    ol = overlap(s1, s2)
    return 1 if width(ol) >= width(s1) or width(ol) >= width(s2) else 0


def overlap(s1, s2):
    return max(s1[0], s2[0]), min(s1[1], s2[1])


def width(s):
    return max(0, s[1] - s[0] + 1)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
