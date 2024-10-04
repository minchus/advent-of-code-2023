from typing import List
import hashlib


def part1(file_path: str) -> int:
    lines = [x.strip() for x in open(file_path).readlines()]

    matrix = [list(s) for s in lines]
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for row in range(n_rows):
        for col in range(n_cols):
            r = row
            if matrix[row][col] == 'O':
                matrix[row][col] = '.'
                while r > 0 and matrix[r - 1][col] == '.':
                    r -= 1
                matrix[r][col] = 'O'


    result = 0
    for row_num, row in enumerate(matrix):
        result += (n_rows - row_num) * row.count('O')

    return result




def part2(file_path: str) -> int:
    lines = [x.strip() for x in open(file_path).readlines()]

    matrix = [list(s) for s in lines]
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    def roll():
        for row in range(n_rows):
            for col in range(n_cols):
                r = row
                if matrix[row][col] == 'O':
                    matrix[row][col] = '.'
                    while r > 0 and matrix[r - 1][col] == '.':
                        r -= 1
                    matrix[r][col] = 'O'

    def rotate_cw():
        nonlocal matrix
        matrix = [list(x) for x in zip(*matrix[::-1])]

    def cycle():
        for _ in range(4):
            roll()
            rotate_cw()

    def print_matrix():
        for row in matrix:
            print(f'{row}')
        print()

    def score():
        ret = 0
        for row_num, row in enumerate(matrix):
            # print(f'{n_rows - row_num} {row}')
            ret += (n_rows - row_num) * row.count('O')
        return ret

    seen = {}
    scores = []
    cycle_start = 0
    cycle_length = 0
    for i in range(500):
        cycle()
        s = score()
        scores.append(s)
        # print(f'{i} {s}')
        h = hashlib.md5(repr(matrix).encode()).hexdigest()
        if h in seen:
            cycle_length = i - seen[h]
            cycle_start = i - cycle_length
            break
        seen[h] = i

    idx = cycle_start + (1000_000_000 - 1 - cycle_start) % cycle_length
    # print(f'cycle_start={cycle_start} cycle_length={cycle_length} idx={idx} score={scores[idx]}')
    return scores[idx]


assert(part1('test.txt') == 136)
print(part1('input.txt'))

assert(part2('test.txt') == 64)
print(part2('input.txt'))




