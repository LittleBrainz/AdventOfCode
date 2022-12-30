# AdventOfCode/2022/day04/solution.py
#
# Day 4: Camp Cleanup
#
# https://adventofcode.com/2022/day/4


from dataclasses import dataclass


@dataclass
class Sections:
    a: int
    b: int

@dataclass
class SectionsPair:
    s1: Sections
    s2: Sections


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[SectionsPair]:
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text: str) -> SectionsPair:
    s1_t, s2_t = line_text.split(",")
    s1a_t, s1b_t = s1_t.split("-")
    s2a_t, s2b_t = s2_t.split("-")
    return SectionsPair(Sections(int(s1a_t), int(s1b_t)), Sections(int(s2a_t), int(s2b_t)))


def calc_part1(sp_list: list[SectionsPair]) -> int:
    return sum(contains(sp) for sp in sp_list)


def calc_part2(sp_list: list[SectionsPair]) -> int:
    return sum(overlaps(sp) for sp in sp_list)


def overlaps(sp: SectionsPair) -> int:
    ol = overlap(sp)
    return 1 if width(ol) > 0 else 0


def contains(sp: SectionsPair) -> int:
    ol = overlap(sp)
    return 1 if width(ol) == width(sp.s1) or width(ol) == width(sp.s2) else 0


def overlap(sp: SectionsPair) -> Sections:
    return Sections(max(sp.s1.a, sp.s2.a), min(sp.s1.b, sp.s2.b))


def width(s: Sections) -> int:
    return max(0, s.b - s.a + 1)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
