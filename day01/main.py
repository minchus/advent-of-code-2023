
def parse(file_path:str):
    with open(file_path) as f:
        lines = f.readlines()
    return lines

def part1(lines: list):
    digit_sum = 0
    for line in lines:
        numbers = [c for c in line if c.isnumeric()]
        two_digit_number = int(numbers[0] + numbers[-1])
        digit_sum += two_digit_number

    return digit_sum

assert part1(parse("test.txt")) == 142
print(part1(parse("input.txt")))

def part2(lines: list):
    valid_digits = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }

    mutated_lines = []
    for line in lines:
        for k, v in valid_digits.items():
            line = line.replace(k, v)
        mutated_lines.append(line)

    return part1(mutated_lines)

assert part2(parse("test2.txt")) == 281
print(part2(parse("input.txt")))







