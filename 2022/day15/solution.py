# AdventOfCode/2022/day15/solution.py
#
# Day 15: Beacon Exclusion Zone
#
# https://adventofcode.com/2022/day/15


from copy import deepcopy

from dataclasses import dataclass


@dataclass
class Vec:
    x: int
    y: int

@dataclass
class SenBea:
    sensor: Vec
    beacon: Vec

@dataclass
class Touch:
    x: int
    count: int
    def __lt__(self, other):
        return self.x < other.x


def main(input_name: str, **kwargs) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data, **kwargs)
    part2 = calc_part2(input_data, **kwargs)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[SenBea]:
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text: str) -> SenBea:
    _, _, sx_t, sy_t, _, _, _, _, bx_t, by_t = line_text.split(" ")
    sensor = Vec(int(sx_t[2:-1]), int(sy_t[2:-1]))
    beacon = Vec(int(bx_t[2:-1]), int(by_t[2:]))
    return SenBea(sensor, beacon)


def calc_part1(senbeas: list[SenBea], row=42) -> int:
    # print_senbeas(senbeas, row)
    touchs = calc_touchs(senbeas, row)
    # print_touchs(touchs)
    return row


def calc_part2(senbeas: list[SenBea], row=42) -> int:
    return 42


def calc_touchs(senbeas: list[SenBea], row: int) -> list[Touch]:
    touchs: list[Touch] = []
    for senbea in senbeas:
        dx = diffx(senbea, row)
        if dx >= 0:
            touchs.append(Touch(senbea.sensor.x - dx, 1))
            touchs.append(Touch(senbea.sensor.x + dx + 1, -1))
    return sorted(touchs)


def calc_touched(touchs: list[Touch]) -> int:
    x0 = -9999999
    count = 0
    touched = 0
    for touch in touchs:
        if x0 != touch.x:
            print(f"       {x0:2d} {'x'*count}")
            x0 = touch.x
        print(f"{touch.x:2d} {touch.count:2d}")
        count += touch.count
    print(f"       {x0:2d} {'x'*count}")


def diffx(senbea: SenBea, row: int) -> int:
    return distance(senbea) - abs(senbea.sensor.y - row)


def distance(senbea: SenBea) -> int:
    return abs(senbea.beacon.x - senbea.sensor.x) + abs(senbea.beacon.y - senbea.sensor.y)


def print_senbeas(senbeas: list[SenBea], row: int) -> None:
    print()
    for senbea in senbeas:
        dist = distance(senbea)
        dx = diffx(senbea, row)
        print(f"sensor({senbea.sensor.x:2d}, {senbea.sensor.y:2d}), " + 
                f"beacon({senbea.beacon.x:2d}, {senbea.beacon.y:2d}), {dist:2d}, {dx:2d}")


def print_touchs(touchs: list[Touch]) -> None:
    x0 = -9999999
    count = 0
    for touch in touchs:
        if x0 != touch.x:
            print(f"       {x0:2d} {'x'*count}")
            x0 = touch.x
        print(f"{touch.x:2d} {touch.count:2d}")
        count += touch.count
    print(f"       {x0:2d} {'x'*count}")


if __name__ == "__main__":
    main("example.txt", row=10)
    # main("input.txt", row=2000000)
