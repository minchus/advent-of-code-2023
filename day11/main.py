import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def parse(file_path: str):
    lines = open(file_path).readlines()
    return np.array([[c for c in line.strip()] for line in lines])


def solve(file_path: str, add_space=1):
    data = parse(file_path)
    r, c = np.where(data == "#")

    empty_r = [i for i in range(len(data)) if all(data[i] == ".")]
    empty_c = [i for i in range(len(data)) if all(data[:, i] == ".")]

    new_r = r + add_space * np.array([r > empty_r[i] for i in range(len(empty_r))]).sum(axis=0)
    new_c = c + add_space * np.array([c > empty_c[i] for i in range(len(empty_c))]).sum(axis=0)

    distances = abs(new_r - new_r.reshape(-1, 1)) + abs(new_c - new_c.reshape(-1, 1))
    return distances.sum() // 2

assert(solve('test.txt') == 374)
print(solve('input.txt'))

assert(solve('test.txt', 9) == 1030)
assert(solve('test.txt', 99) == 8410)
print(solve('input.txt', 999_999))
