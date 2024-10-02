from typing import List


def parse(file_path):
    lines = open(file_path).readlines()

    input = []
    grid = []
    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            input.append(grid)
            grid = []
        else:
            grid.append(stripped_line)

    if len(grid) > 0:
        input.append(grid)

    return input


def horizontal_axis(problem: List[str]) -> int:
    length = len(problem)
    for i in range(1, length):
        n = min(i, length - i)
        top = problem[i - n : i]
        bottom = problem[i : i + n]
        if top == bottom[::-1]:
            return i

    return 0


def part1(file_path):
    input = parse(file_path)
    result = 0
    for problem in input:
        h_axis = horizontal_axis(problem)
        transposed = [''.join(s) for s in zip(*problem)]
        v_axis = horizontal_axis(transposed)
        result += (v_axis + 100 * h_axis)

    return result

assert(part1('test.txt') == 405)
print(part1('input.txt'))


def horizontal_axis_2(problem: List[str]) -> int:
    length = len(problem)
    for i in range(1, length):
        n = min(i, length - i)
        top = problem[i - n : i]
        bottom = problem[i : i + n]
        diff_count = 0
        for top_, bottom_ in zip(top, bottom[::-1]):
            diff_count += sum(1 for a, b in zip(top_, bottom_) if a != b)

        if diff_count == 1:
            return i

    return 0


def part2(file_path):
    input = parse(file_path)
    result = 0
    for problem in input:
        h_axis = horizontal_axis_2(problem)

        transposed = [''.join(s) for s in zip(*problem)]
        v_axis = horizontal_axis_2(transposed)

        assert(h_axis == 0 or v_axis == 0)
        result += (v_axis + 100 * h_axis)

    return result


assert(part2('test.txt') == 400)
assert(part2('test2.txt') == 5)
print(part2('input.txt'))



