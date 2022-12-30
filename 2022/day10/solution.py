# AdventOfCode/2022/day10/solution.py
#
# Day 10: Cathode-Ray Tube
#
# https://adventofcode.com/2022/day/10


from dataclasses import dataclass


@dataclass
class Opcode:
    op:  str
    arg: int


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[Opcode]:
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text: str) -> Opcode:
    tokens = line_text.split(" ")
    op = tokens[0]
    arg = int(tokens[1]) if len(tokens) == 2 else 0
    return Opcode(op, arg)


def calc_part1(opcode_list: list[Opcode]) -> None:
    cpu = CPU(opcode_list)
    return cpu.signal


def calc_part2(opcode_list: list[Opcode]) -> None:
    cpu = CPU(opcode_list)
    return '\n' + cpu.get_crt()


class CPU:
    def __init__(self, opcode_list: list[Opcode]) -> None:
        self.clock = 1
        self.reg_X = 1
        self.signal = 0
        self.crt = CRT()
        for opcode in opcode_list:
            self.execute(opcode)

    def execute(self, opcode: Opcode) -> None:
        if opcode.op == "noop":
            self.cycle()
        if opcode.op == "addx":
            self.cycle()
            self.cycle()
            self.reg_X += opcode.arg
    
    def cycle(self) -> None:
        if (self.clock + 20) % 40 == 0:
            self.signal += self.clock * self.reg_X
        self.crt.cycle(self.clock, self.reg_X)
        self.clock += 1

    def get_crt(self) -> str:
        return str(self.crt)


class CRT:
    def __init__(self) -> None:
        self.video = [["."] * 40 for _ in range(6)]

    def __str__(self) -> str:
        return '\n'.join(''.join(pixels) for pixels in self.video)

    def cycle(self, clock: int, reg_X: int) -> None:
        line = (clock - 1) // 40
        pixl = (clock - 1) % 40
        if abs(pixl - reg_X) <= 1:
            self.video[line][pixl] = "#"


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
