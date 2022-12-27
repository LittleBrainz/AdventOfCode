# AdventOfCode/2022/day08/solution.py
#
# Day 8: Treetop Tree House
#
# https://adventofcode.com/2022/day/8


import numpy as np


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text: str):
    inp_grid = [parse_line(input_line) for input_line in input_text.split("\n")]
    rows = len(inp_grid)
    cols = len(inp_grid[0])
    vis_grid = [[0] * cols for _ in range(rows)]
    return (inp_grid, vis_grid, rows, cols)


def parse_line(input_line: str) -> list[int]:
    return [int(char) for char in input_line]


def calc_part1(input_data: tuple) -> int:
    (inp_grid, vis_grid, rows, cols) = input_data
    for i in range(4):
        inp_grid = rotate_grid(inp_grid, rows, cols)
        vis_grid = rotate_grid(vis_grid, rows, cols)
        vis_grid = scan_grid(inp_grid, vis_grid)
    return sum(sum(vis_row) for vis_row in vis_grid)


def calc_part2(input_data) -> int:
    return 0


def scan_grid(inp_grid: list[list[int]], vis_grid: list[list[int]]) -> list[list[int]]:
    return [scan_row(inp_row, vis_row)
            for (inp_row, vis_row) in zip(inp_grid, vis_grid)]


def scan_row(inp_row: list[int], vis_row: list[int]) -> list[int]:
    high = -1
    for col in range(len(inp_row)):
        if high < inp_row[col]:
            high = inp_row[col]
            vis_row[col] = 1
    return vis_row


def scan_grid_np(array: np.ndarray, rot90: int) -> np.ndarray:
    rotated = np.rot90(array, rot90)
    padded  = np.pad(rotated, ((1,0),(0,0)), constant_values=-1)
    greater = np.greater(padded[1:], padded[:-1])
    fixed = np.rot90(greater, -rot90)
    print(fixed)
    return fixed


def rotate_grid(org_grid: list[list[int]], rows: int, cols: int) -> list[list[int]]:
    rot_grid = [[0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            rot_grid[col][rows-row-1] = org_grid[row][col]
    return rot_grid


def print_grid(grid):
    for row_cells in grid:
        for cell in row_cells:
            print(f"{cell:3d}", end="")
        print()
    print()


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
