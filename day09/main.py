import re


def parse(file_path: str):
    ret = []
    with open(file_path) as f:
        for line in f.readlines():
            vals = [int(v) for v in line.split()]
            ret.append(vals)

    return ret


def part1(file_path: str):
    def diff(a: list):
        if (all(x == a[0] for x in a)):
            return a[0]

        diffs = [x - y for x, y in zip(a[1:], a)]
        return a[-1] + diff(diffs)

    vals = parse(file_path)
    return sum(diff(v) for v in vals)


def part2(file_path: str):
    def diff(a: list):
        if (all(x == a[0] for x in a)):
            return a[0]

        diffs = [x - y for x, y in zip(a[1:], a)]
        return a[0] - diff(diffs)

    vals = parse(file_path)
    return sum(diff(v) for v in vals)


assert(part1('test.txt') == 114)
print(part1('input.txt'))

assert(part2('test.txt') == 2)
print(part2('input.txt'))
