from functools import cache

def parse(file_path: str):
    lines = open(file_path).readlines()
    return lines


@cache
def arrangements(conditions, rules):
    if not rules:
        return 0 if '#' in conditions else 1
    if not conditions:
        return 1 if not rules else 0

    ret = 0

    if conditions[0] in '.?':
        ret += arrangements(conditions[1:], rules)
    if conditions[0] in '#?':
        if (
            rules[0] <= len(conditions)
            and '.' not in conditions[:rules[0]]
            and (rules[0] == len(conditions) or conditions[rules[0]] != '#')
        ):
            ret += arrangements(conditions[rules[0] + 1:], rules[1:])

    return ret


def part1(file_path: str):
    lines = parse(file_path)
    result = 0
    for line in lines:
        conditions, rules = line.split()
        rules = eval(rules)
        result += arrangements(conditions, rules)

    return result


def part2(file_path: str):
    lines = parse(file_path)
    result = 0
    for line in lines:
        conditions, rules = line.split()
        rules = eval(rules)

        conditions = '?'.join([conditions] * 5)
        rules = rules * 5
        result += arrangements(conditions, rules)

    return result


assert(part1('test.txt') == 21)
print(part1('input.txt'))

assert(part2('test.txt') == 525152)
print(part2('input.txt'))
