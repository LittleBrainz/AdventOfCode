# AdventOfCode/2022/day06/solution.py
#
# Day 6: Tuning Trouble
#
# https://adventofcode.com/2022/day/6


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[str]:
    return input_text.split("\n")


def calc_part1(buffer_list: list[str]) -> list[int]:
    return [marker_pos(buffer, 4) for buffer in buffer_list]


def calc_part2(buffer_list: list[str]) -> list[int]:
    return [marker_pos(buffer, 14) for buffer in buffer_list]


def marker_pos(buffer: str, width: int) -> int:
    for i in range(len(buffer) - (width - 1)):
        marker = buffer[i:i+width]
        if len(set(marker)) == width:
            return i + width
    return 0


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
