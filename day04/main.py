
def parse(file_path: str):
    with open(file_path) as f:
        lines = f.readlines()

    cards = []
    for line in lines:
        line = line.split(':')[1]
        winners = line.split('|')[0].strip().split()
        ours = line.split('|')[1].strip().split()
        cards.append([winners, ours])

    return cards


def part1(file_path):
    cards = parse(file_path)

    result = 0
    for card in cards:
        winners = card[0]
        ours = card[1]
        intersection = len(set(winners) & set(ours))
        if intersection > 0:
            result += pow(2, intersection - 1)

    return result


def part2(file_path):
    cards = parse(file_path)

    copy_count = [1 for _ in range(len(cards))]

    for index, card in enumerate(cards):

        winners = card[0]
        ours = card[1]
        intersection = len(set(winners) & set(ours))

        for i in range(intersection):
            copy_count[index + 1 + i] += copy_count[index]

    return sum(copy_count)

p1 = part1('test.txt')
expected = 13
assert(p1 == expected), (p1, expected)
print(part1('input.txt'))

p2 = part2('test.txt')
expected = 30
assert(p2 == expected), (p2, expected)
print(part2('input.txt'))

