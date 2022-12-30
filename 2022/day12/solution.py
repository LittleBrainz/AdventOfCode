# AdventOfCode/2022/day12/solution.py
#
# Day 12: Hill Climbing Algorithm
#
# https://adventofcode.com/2022/day/12


import sys

from dataclasses import dataclass


@dataclass
class Cell:
    height: int
    steps: int

@dataclass
class Pos:
    row: int
    col: int

@dataclass
class Grid:
    cells: list[list[Cell]]
    rows:  int
    cols:  int
    start: Pos


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[list[Cell]]:
    line_text_list = input_text.split("\n")
    rows = len(line_text_list) + 2
    cols = len(line_text_list[0]) + 2
    cells = [[Cell(99, 9999) for _ in range(cols)] for _ in range(rows)]
    for row in range(1, rows - 1):
        line_text = line_text_list[row - 1]
        for col in range(1, cols - 1):
            letter = line_text[col - 1]
            if letter == "S":
                start = Pos(row, col)
            cell = cells[row][col]
            cell.height = "SabcdefghijklmnopqrstuvwxyzE".index(letter) - 1
    return Grid(cells, rows, cols, start)


def calc_part1(grid: Grid) -> int:
    return explore(grid, grid.start, 0)


def calc_part2(grid: Grid) -> int:
    min_steps = explore(grid, grid.start, 0)
    for row in range(1, grid.rows - 1):
        for col in range(1, grid.cols - 1):
            if grid.cells[row][col].height == 0:
                min_steps = min(min_steps, explore(grid, Pos(row, col), 0))
    return min_steps


def explore(grid: Grid, pos: Pos, steps: int) -> int:
    cell = grid.cells[pos.row][pos.col]
    cell.steps = steps
    if cell.height == 26:
        return steps
    min_steps = 9999
    for (drow, dcol) in ((1,0), (0,1), (-1,0), (0,-1)):
        ex_pos = Pos(pos.row + drow, pos.col + dcol)
        ex_cell = grid.cells[ex_pos.row][ex_pos.col]
        if ex_cell.height <= cell.height + 1 and ex_cell.steps > steps + 1:
            min_steps = min(min_steps, explore(grid, ex_pos, steps + 1))
    return min_steps


def print_grid(grid: Grid):
    print(f"\nrows = {grid.rows}  cols = {grid.cols}  start = {grid.start}\n")
    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.cells[row][col]
            print(f"{cell.height:3d}", end="")
        print()


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    main("example.txt")
    main("input.txt")
