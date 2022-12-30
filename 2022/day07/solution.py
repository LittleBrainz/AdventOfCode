# AdventOfCode/2022/day07/solution.py
#
# Day 7: No Space Left On Device
#
# https://adventofcode.com/2022/day/7


from dataclasses import dataclass


@dataclass
class Node:
    type: str
    parent: object
    size: int
    children: dict = None


def main(input_name: str) -> None:
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    part1 = calc_part1(input_data)
    part2 = calc_part2(input_data)
    print(f"\n{input_name}:\n  Part 1 = {part1}\n  Part 2 = {part2}")


def parse_input(input_text: str) -> Node:
    root_node = Node("dir", None, 0, {})
    this_node = root_node
    for line_text in input_text.split("\n"):
        this_node = parse_line(line_text, this_node, root_node)
    bubble_size(root_node)
    # print_node(0, "/", root_node)
    return root_node


def parse_line(line_text: str, this_node: Node, root_node: Node) -> Node:
    if line_text[0:4] == "$ cd":
        dir_name = line_text[5:]
        if dir_name == "/":
            return root_node
        if dir_name == "..":
            return this_node.parent
        return this_node.children[dir_name]
    if line_text[0:4] == "$ ls":
        return this_node
    size_t, name = line_text.split(" ")
    if size_t == "dir":
        node = Node("dir", this_node, 0, {})
    else:
        node = Node("file", this_node, int(size_t))
    this_node.children[name] = node
    return this_node


def bubble_size(this_node: Node) -> int:
    if this_node.type == "dir":
        this_node.size = sum(bubble_size(node)
                for node in this_node.children.values())
    return this_node.size


def calc_part1(root_node: Node) -> int:
    sizes = [size for size in get_dir_sizes(root_node) if size <= 100000]
    return sum(sizes)


def calc_part2(root_node: Node) -> int:
    required_size = 30000000 - (70000000 - root_node.size)
    sizes = [size for size in get_dir_sizes(root_node) if size >= required_size]
    return sizes[0]


def get_dir_sizes(this_node: Node) -> list[int]:
    if this_node.type == "file":
        return []
    sizes = [this_node.size]
    for node in this_node.children.values():
        sizes += get_dir_sizes(node)
    return sorted(sizes)


def print_node(indent: int, this_name: str, this_node: Node) -> None:
    print(f"{'  '*indent}- {this_name} ({this_node.type}, size={this_node.size})")
    if this_node.type == "file":
        return
    for (name, node) in this_node.children.items():
        print_node(indent + 1, name, node)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
