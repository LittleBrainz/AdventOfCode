# AdventOfCode/2023/day01/solution.py
#
# Day 1: Trebuchet?!
#
# https://adventofcode.com/2023/day/1


import re


word_digits = {
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0',
}

words_pattern = '|'.join(word_digits.keys())

words_regex = re.compile(f'(?=({words_pattern}))')


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> list[str]:
    return [line for line in text.split('\n')]


def calc_part_1(data: list[str]) -> int:
    return sum([int(get_first_last_digits_1(line)) for line in data])


def calc_part_2(data: list[str]) -> int:
    return sum([int(get_first_last_digits_2_re(line)) for line in data])


def get_first_last_digits_1(line: str) -> str:
    digits = list(filter(lambda c: c.isdigit(), line))
    return digits[0] + digits[-1] if len(digits) > 0 else '0'


def get_first_last_digits_2(line: str) -> str:
    return get_first_digit(line) + get_last_digit(line)


def get_first_last_digits_2_re(line: str) -> str:
    words = words_regex.findall(line)
    return word_digits[words[0]] + word_digits[words[-1]]


def get_first_digit(line: str) -> str:
    for i in range(len(line)):
        for word, digit in word_digits.items():
            if line[i:].startswith(word):
                return digit
    return '0'


def get_last_digit(line: str) -> str:
    for i in range(len(line) + 1, 0, -1):
        for word, digit in word_digits.items():
            if line[:i].endswith(word):
                return digit
    return '0'


if __name__ == '__main__':
    # main('example1.txt')
    # main('example2.txt')
    main('input.txt')
