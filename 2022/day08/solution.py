# AdventOfCode/2022/day08/solution.py
#
# Day 8: Treetop Tree House
#
# https://adventofcode.com/2022/day/8


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> list[list[int]]:
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text: str) -> list[int]:
    return [int(char) for char in line_text]


def calc_part1(inp_grid: list[list[int]]) -> int:
    vis_grid = calc_vis_grid(inp_grid, vis_init=0, scan_row_fn=scan_row1)
    return sum(sum(vis_row) for vis_row in vis_grid)


def calc_part2(inp_grid: list[list[int]]) -> int:
    vis_grid = calc_vis_grid(inp_grid, vis_init=1, scan_row_fn=scan_row2)
    return max(max(vis_row) for vis_row in vis_grid)


def calc_vis_grid(inp_grid: list[list[int]], vis_init: int, 
        scan_row_fn) -> list[list[int]]:
    rows = len(inp_grid)
    cols = len(inp_grid[0])
    vis_grid = [[vis_init] * cols for _ in range(rows)]
    for i in range(4):
        inp_grid = rotate_grid(inp_grid)
        vis_grid = rotate_grid(vis_grid)
        vis_grid = scan_grid(inp_grid, vis_grid, scan_row_fn)
    return vis_grid


def scan_grid(inp_grid: list[list[int]], vis_grid: list[list[int]],
        scan_row_fn) -> list[list[int]]:
    return [scan_row_fn(inp_row, vis_row)
            for (inp_row, vis_row) in zip(inp_grid, vis_grid)]


def scan_row1(inp_row: list[int], vis_row: list[int]) -> list[int]:
    height = -1
    for col in range(len(inp_row)):
        if height < inp_row[col]:
            height = inp_row[col]
            vis_row[col] = 1
    return vis_row


def scan_row2(inp_row: list[int], vis_row: list[int]) -> list[int]:
    last_col = [0] * (9 + 1)
    for col in range(len(inp_row)):
        height = inp_row[col]
        vis_row[col] *= col - last_col[height]
        last_col[:height+1] = [col] * (height + 1)
    return vis_row


def rotate_grid(org_grid: list[list[int]]) -> list[list[int]]:
    rows = len(org_grid)
    cols = len(org_grid[0])
    rot_grid = [[0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            rot_grid[col][rows-row-1] = org_grid[row][col]
    return rot_grid


def print_grid(grid: list[list[int]]) -> None:
    for row_cells in grid:
        for cell in row_cells:
            print(f"{cell:3d}", end="")
        print()
    print()


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
