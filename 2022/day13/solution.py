# AdventOfCode/2022/day13/solution.py
#
# Day 13: Distress Signal
#
# https://adventofcode.com/2022/day/13


from functools import cmp_to_key


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[tuple[list, list]]:
    return [parse_group(group_text) for group_text in input_text.split("\n\n")]


def parse_group(group_text: str) -> tuple[list, list]:
    line0_text, line1_text = group_text.split("\n")
    return (parse_line(line0_text), parse_line(line1_text))


def parse_line(line_text: str) -> list:
    return parse_list(line_text, 1)[0]


def parse_list(text: str, i: int) -> list:
    list1 = []
    numbr = 0
    digit = False
    while i < len(text):
        char = text[i]
        i += 1
        if char == "[":
            (list2, i) = parse_list(text, i)
            list1.append(list2)
        if char.isdigit():
            numbr = numbr * 10 + int(char)
            digit = True
        if char == ",":
            if digit:
                list1.append(numbr)
                numbr = 0
                digit = False
        if char == "]":
            if digit:
                list1.append(numbr)
            return (list1, i)
    return None


def calc_part1(input_data: list[tuple[list, list]]) -> int:
    index_total = 0
    for (index, (list1, list2)) in enumerate(input_data):
        if calc_order(list1, list2) <= 0:
            index_total += (index + 1)
    return index_total


def calc_part2(input_data: list[tuple[list, list]]) -> int:
    divider1 = parse_line("[[2]]")
    divider2 = parse_line("[[6]]")
    big_list = []
    for (list1, list2) in input_data:
        big_list.append(list1)
        big_list.append(list2)
    big_list.append(divider1)
    big_list.append(divider2)
    big_list.sort(key=cmp_to_key(calc_order))
    index1 = big_list.index(divider1) + 1
    index2 = big_list.index(divider2) + 1
    return index1 * index2


def calc_order(list1: list, list2: list) -> int:
    for (item1, item2) in zip(list1, list2):
        if type(item1) == int and type(item2) == int:
            if item1 != item2:
                return item1 - item2
            continue
        if type(item1) == int:
            item1 = [item1]
        if type(item2) == int:
            item2 = [item2]
        order = calc_order(item1, item2)
        if order != 0:
            return order
    if len(list1) != len(list2):
        return len(list1) - len(list2)
    return 0


def print_data(input_data: list[tuple[list, list]]) -> None:
    for (list1, list2) in input_data:
        print()
        print(list1)
        print(list2)


def print_big_list(big_list: list[list], index1: int, index2: int) -> None:
    print()
    for list in big_list:
        print(list)
    print(f"\nindex1 = {index1}, index2 = {index2}")


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
