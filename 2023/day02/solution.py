# AdventOfCode/2023/day02/solution.py
#
# Day 2: Cube Conundrum
#
# https://adventofcode.com/2023/day/2


from dataclasses import dataclass


@dataclass
class CubeSet:
    r: int
    g: int
    b: int


@dataclass
class Game:
    id: int
    cubesets: list[CubeSet]


def main(path: str) -> None:
    text = open(path).read().rstrip()
    data = parse_text(text)
    part_1 = calc_part_1(data)
    part_2 = calc_part_2(data)
    print(f'\n{path}:\n  Part 1 = {part_1}\n  Part 2 = {part_2}')


def parse_text(text: str) -> list[Game]:
    return [parse_game_s(game_s) for game_s in text.split('\n')]


def parse_game_s(game_s: str) -> Game:
    (id_s, cubesets_s) = game_s.split(': ')
    id = int(id_s.split(' ')[1])
    cubesets = [parse_cubeset_s(cubeset_s) for cubeset_s in cubesets_s.split('; ')]
    return Game(id, cubesets)


def parse_cubeset_s(cubeset_s: str) -> CubeSet:
    cubeset = CubeSet(0, 0, 0)
    for cube_s in cubeset_s.split(', '):
        (val_s, color_s) = cube_s.split(' ')
        setattr(cubeset, color_s[0], int(val_s))
    return cubeset


def calc_part_1(games: list[Game]) -> int:
    id_total = 0
    max_cubeset = CubeSet(12, 13, 14)
    for game in games:
        id = game.id
        for cubset in game.cubesets:
            if (cubset.r > max_cubeset.r or
                cubset.g > max_cubeset.g or
                cubset.b > max_cubeset.b):
                id = 0
        id_total += id
    return id_total


def calc_part_2(games: list[Game]) -> int:
    power_total = 0
    for game in games:
        max_cubeset = CubeSet(0, 0, 0)
        for cubset in game.cubesets:
            max_cubeset.r = max(max_cubeset.r, cubset.r)
            max_cubeset.g = max(max_cubeset.g, cubset.g)
            max_cubeset.b = max(max_cubeset.b, cubset.b)
        power_total += max_cubeset.r * max_cubeset.g * max_cubeset.b
    return power_total


if __name__ == '__main__':
    # main('example.txt')
    main('input.txt')
