import math


def parse(file_path: str):
    with open(file_path) as f:
        return [l.strip() for l in f.readlines()]


def find_start(lines):
    for row, l in enumerate(lines):
        if 'S' in l:
            return row, l.index('S')


def next_pos(row, col, lines, visited):
    visited[row][col] = True
    cur_tile = lines[row][col]

    def get_next(directions):
        for d in directions:
            next_r = row + d[0]
            next_c = col + d[1]
            valid_symbols = d[2] if len(d) > 2 else '-|7LJF'

            if (next_r >= 0 and next_r < len(lines) and next_c >= 0 and next_c < len(lines[0])
                and lines[next_r][next_c] in valid_symbols and not visited[next_r][next_c]):
                return next_r, next_c
        return -1, -1

    if cur_tile == 'S':
        next_row, next_col = get_next([ [0, 1, '-J7'], [1, 0, '|LJ'], [0, -1, '-LF'], [-1, 0, '|7F'] ])
    elif cur_tile == '|':
        next_row, next_col = get_next([ [1, 0], [-1, 0] ])
    elif cur_tile == '-':
        next_row, next_col = get_next([ [0, 1], [0, -1] ])
    elif cur_tile == '7':
        next_row, next_col = get_next([ [0, -1], [1, 0] ])
    elif cur_tile == 'L':
        next_row, next_col = get_next([ [-1, 0], [0, 1] ])
    elif cur_tile == 'F':
        next_row, next_col = get_next([ [0, 1], [1, 0] ])
    elif cur_tile == 'J':
        next_row, next_col = get_next([ [-1, 0], [0, -1] ])
    else:
        raise Exception(f'Unknown tile')

    return next_row, next_col


def part1(file_path: str):

    lines = parse(file_path)
    visited = [[False for col in range(len(lines[0]))] for row in range(len(lines))]
    row, col = find_start(lines)
    step = 0
    while row >= 0:
        # print(f'{step} grid[{row}][{col}]={lines[row][col]}')
        row, col = next_pos(row, col, lines, visited)
        step += 1

    return math.ceil(step / 2)


def polygon_area(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return 0.5 * abs(area)


def part2(file_path: str):

    lines = parse(file_path)
    visited = [[False for col in range(len(lines[0]))] for row in range(len(lines))]
    row, col = find_start(lines)
    step = 0

    vertices = []
    while row >= 0:
        # print(f'{step} grid[{row}][{col}]={lines[row][col]}')
        if lines[row][col] in '7LFJS':
            vertices.append([row, col])
        row, col = next_pos(row, col, lines, visited)
        step += 1

    return polygon_area(vertices) + 1 - step / 2


assert(part1('test.txt') == 4)
assert(part1('test1.txt') == 8)
print(part1('input.txt'))

assert(part2('test.txt') == 1)
assert(part2('test2.txt') == 4)
assert(part2('test3.txt') == 8)
print(part2('input.txt'))


