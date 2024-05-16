
def parse(file_path: str):
    with open(file_path) as f:
        lines = f.readlines()

    tokens = []
    symbols = []
    for row, line in enumerate(lines):
        token = ''
        coords = []
        for col, char in enumerate(line):
            if char.isnumeric():
                token += char
                coords.append((row, col))
            else:
                if len(token) > 0:
                    tokens.append((token, coords))
                    token = ''
                    coords = []

                if char != '.' and char != '\n':
                    symbols.append((row, col, char))
    return lines, tokens, symbols

def get_adjacent(symbols: list, n_row: int, n_col: int):
    adjacent = dict()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row, col, _ in symbols:
        for dir_row, dir_col in directions:
            next_row = row + dir_row
            next_col = col + dir_col
            if next_row >= 0 and next_row <= n_row and next_col >=0 and next_col <= n_col:
                adjacent[(next_row, next_col)] = (row, col)

    return adjacent


def part1(file_path: str):
    lines, tokens, symbols = parse(file_path)
    n_col = len(lines[0].strip())
    n_row = len(lines)
    # for l in lines:
    #     print(l.strip())
    # for t in tokens:
    #     print(t)
    # print(f'symbols={symbols}')

    adjacent = get_adjacent(symbols, n_row, n_col)
    # print(f'adjacent={adjacent}')

    valid_tokens = []
    for token_string, coords in tokens:
        for c in coords:
            if c in adjacent.keys():
                valid_tokens.append(int(token_string))
                break

    # print(f'valid_tokens={valid_tokens}')
    return sum(valid_tokens)

def part2(file_path: str):
    lines, tokens, symbols = parse(file_path)
    n_col = len(lines[0].strip())
    n_row = len(lines)
    symbols = list(filter(lambda x: x[2] == '*', symbols))
    # for l in lines:
    #     print(l.strip())
    # for t in tokens:
    #     print(t)
    # print(f'symbols={symbols}')

    adjacent = get_adjacent(symbols, n_row, n_col)
    # print(f'adjacent={adjacent}')

    valid_tokens = {}
    for token_string, coords in tokens:
        for c in coords:
            if c in adjacent:
                symbol_coord = adjacent[c]
                if symbol_coord in valid_tokens:
                    valid_tokens[symbol_coord].append(int(token_string))
                else:
                    valid_tokens[symbol_coord] = [int(token_string)]
                break

    # print(f'valid_tokens={valid_tokens}')
    result = 0
    for _, adjacent_nums in valid_tokens.items():
        if len(adjacent_nums) == 2:
            result += adjacent_nums[0] * adjacent_nums[1]

    return result


assert(part1('test.txt') == 4361)
print(part1('input.txt'))

assert(part2('test.txt') == 467835)
print(part2('input.txt'))
