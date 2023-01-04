# AdventOfCode/2022/day14/solution.py
#
# Day 14: Regolith Reservoir
#
# https://adventofcode.com/2022/day/14


from copy import deepcopy

from dataclasses import dataclass


@dataclass
class Vec:
    x: int
    y: int

@dataclass
class Line:
    v0: Vec
    vs: list[Vec]

@dataclass
class Grid:
    lines: list[Line]
    sand: Vec
    minv: Vec
    maxv: Vec
    cells: list[list[str]]


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> Grid:
    lines = [parse_line(line_text) for line_text in input_text.split("\n")]
    sand = Vec(500, 0)
    (minv, maxv) = get_min_max(lines, sand)
    cells = [["."] * (maxv.x - minv.x + 1) for _ in range(maxv.y - minv.y + 1)]
    grid = Grid(lines, sand, minv, maxv, cells)
    set_cell(grid, sand, "+")
    draw_lines(grid)
    return grid


def parse_line(line_text: str) -> Line:
    vs = [parse_vec(vec_text) for vec_text in line_text.split(" -> ")]
    return Line(vs[0], vs[1:])


def parse_vec(vec_text: str) -> Vec:
    x_t, y_t = vec_text.split(",")
    return Vec(int(x_t), int(y_t))


def get_min_max(lines: list[Line], sand: Vec) -> tuple[Vec, Vec]:
    minv = sand
    maxv = sand
    for line in lines:
        (minv, maxv) = vec_min_max(minv, maxv, line.v0)
        for v in line.vs:
            (minv, maxv) = vec_min_max(minv, maxv, v)
    maxv.y += 2
    minv.x = min(minv.x, sand.x - (maxv.y - sand.y) - 1)
    maxv.x = max(maxv.x, sand.x + (maxv.y - sand.y) + 1)
    return (minv, maxv)


def vec_min_max(minv: Vec, maxv: Vec, v: Vec) -> tuple[Vec, Vec]:
    return (Vec(min(minv.x, v.x), min(minv.y, v.y)), 
            Vec(max(maxv.x, v.x), max(maxv.y, v.y)))


def draw_lines(grid: Grid) -> None:
    for line in grid.lines:
        v0 = line.v0
        for v1 in line.vs:
            draw_line(grid, v0, v1)
            v0 = v1


def draw_line(grid: Grid, v0: Vec, v1: Vec) -> None:
    if v0.x != v1.x:
        for x in myrange(v0.x, v1.x):
            set_cell(grid, Vec(x, v0.y), "#")
    else:
        for y in myrange(v0.y, v1.y):
            set_cell(grid, Vec(v0.x, y), "#")


def calc_part1(grid: Grid) -> int:
    grid = deepcopy(grid)
    units = 0
    while drop_sand(grid):
        units += 1
    return units


def calc_part2(grid: Grid) -> int:
    grid = deepcopy(grid)
    draw_line(grid, Vec(grid.minv.x, grid.maxv.y), grid.maxv)
    units = 0
    while get_cell(grid, grid.sand) != "o":
        drop_sand(grid)
        units += 1
    return units


def drop_sand(grid: Grid) -> Vec:
    v0 = grid.sand
    while v0.y < grid.maxv.y:
        v = drip_sand(grid, v0)
        if v == v0:
            set_cell(grid, v0, "o")
            return True
        v0 = v
    return False


def drip_sand(grid: Grid, v0: Vec) -> Vec:
    for x in (0, -1, 1):
        v = Vec(v0.x + x, v0.y + 1)
        if get_cell(grid, v) == ".":
            return v
    return v0


def print_grid(grid: Grid) -> None:
    # print()
    # for line in grid.lines:
    #     print(f"{line.v0.x},{line.v0.y}", end="")
    #     for v in line.vs:
    #         print(f" -> {v.x},{v.y}", end="")
    #     print()
    print(f"\nmin = {grid.minv.x},{grid.minv.y}, max = {grid.maxv.x},{grid.maxv.y}\n")
    for y in myrange(grid.minv.y, grid.maxv.y):
        for x in myrange(grid.minv.x, grid.maxv.x):
            print(get_cell(grid, Vec(x, y)), end="")
        print()


def get_cell(grid: Grid, v: Vec) -> str:
    if v.x < grid.minv.x or grid.maxv.x < v.x or v.y < grid.minv.y or grid.maxv.y < v.y:
        return "."
    return grid.cells[v.y - grid.minv.y][v.x - grid.minv.x]


def set_cell(grid: Grid, v: Vec, cell: str) -> None:
    grid.cells[v.y - grid.minv.y][v.x - grid.minv.x] = cell


def myrange(i0: int, i1: int):
    step = 1 if i0 <= i1 else -1
    i1 += step
    i = i0
    while i != i1:
        yield i
        i += step


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
