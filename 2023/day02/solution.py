# AdventOfCode/2023/day02/solution.py
#
# Day 2: Cube Conundrum
#
# https://adventofcode.com/2023/day/2


from dataclasses import dataclass


@dataclass
class CubeSet:
    red: int
    green: int
    blue: int


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
    game = Game(id, cubesets)
    return game


def parse_cubeset_s(cubeset_s: str) -> CubeSet:
    cubeset = CubeSet(0, 0, 0)
    for cube_s in cubeset_s.split(', '):
        (val_s, color_s) = cube_s.split(' ')
        setattr(cubeset, color_s, int(val_s))
    return cubeset


def calc_part_1(games: list[Game]) -> int:
    max_cubeset = parse_cubeset_s('12 red, 13 green, 14 blue')
    id_count = 0
    for game in games:
        id = game.id
        for cubset in game.cubesets:
            if (cubset.red > max_cubeset.red or
                cubset.green > max_cubeset.green or
                cubset.blue > max_cubeset.blue):
                id = 0
        id_count += id
    return id_count


def calc_part_2(games: list[Game]) -> int:
    return 0


if __name__ == '__main__':
    # main('example.txt')
    main('input.txt')
