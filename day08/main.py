import math
import re

from itertools import cycle


def parse(file_path: str):
    with open(file_path) as f:
        directions = [0 if d == 'L' else 1 for d in f.readline().strip()]
        matches = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', f.read())
        return directions, matches


def part1(file_path: str):
    directions, matches = parse(file_path)
    graph = {a: (b, c) for a, b, c in matches}

    node = 'AAA'
    for steps, d in enumerate(cycle(directions), start=1):
        node = graph[node][d]
        if node == 'ZZZ':
            break

    return steps


def part2(file_path: str):
    directions, matches = parse(file_path)
    graph = {a: (b, c) for a, b, c in matches}
    start_nodes = [m for m in graph.keys() if m.endswith('A')]
    cycles = []

    for node in start_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = graph[node][d]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    return math.lcm(*cycles)


assert(part1('test.txt') == 2)
assert(part1('test1.txt') == 6)
print(part1('input.txt'))

assert(part2('test2.txt') == 6)
print(part2('input.txt'))
