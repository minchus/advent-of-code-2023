import math
import re


def parse(file_path):
    with open(file_path) as f:
        times = []
        for t in re.findall(r'(\d+)', f.readline()):
            times.append(int(t))

        dists = []
        for d in re.findall(r'(\d+)', f.readline()):
            dists.append(int(d))

    return times, dists


def solve_quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    return x1, x2  # x1 is always the larger of the two results


def part1(file_path):
    times, dists = parse(file_path)
    # print(times)
    # print(dists)

    ways = []
    for t, d in zip(times, dists):
        x1, x2 = solve_quadratic(1, -t, d)
        w = int(math.ceil(x1)-1) - (math.floor(x2)+1) + 1
        # print(f'x1={x1} x2={x2} ways={w}')
        ways.append(w)

    result = 1
    for w in ways:
        result *= w

    return result

assert(288 == part1('test.txt'))
print(part1('input.txt'))

def part2(file_path):
    times, dists = parse(file_path)
    t = int(''.join(str(x) for x in times))
    d = int(''.join(str(x) for x in dists))
    x1, x2 = solve_quadratic(1, -t, d)
    w = int(math.ceil(x1)-1) - (math.floor(x2)+1) + 1
    print(f'x1={x1} x2={x2} ways={w}')
    return w

assert(71503 == part2('test.txt'))
print(part2('input.txt'))
