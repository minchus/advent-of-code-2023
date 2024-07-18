import re
from collections import Counter

def hand_type(hand: str):
    char_count = {}
    for c in hand:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    occurrences = list(char_count.values())

    # Five of a kind {'A': 5}
    if occurrences.count(5):
        return 6
    # Four of a kind {'A': 4, 'B': 1}
    elif occurrences.count(4):
        return 5
    # Full house {'A': 3, 'B': 2}
    elif occurrences.count(3) == 1 and occurrences.count(2) == 1:
        return 4
    # Three of a kind {'A': 3, 'B': 1, 'C': 1}
    elif occurrences.count(3):
        return 3
    # Two pair {'A': 2, 'B': 2, 'C': 1}
    elif occurrences.count(2) == 2:
        return 2
    # One pair {'A': 2, 'B': 1, 'C': 1, 'D': 1}
    elif occurrences.count(2) == 1:
        return 1

    return 0

assert(hand_type('AAAAA') == 6)
assert(hand_type('AA8AA') == 5)
assert(hand_type('23332') == 4)
assert(hand_type('TTT98') == 3)
assert(hand_type('23432') == 2)
assert(hand_type('A23A4') == 1)
assert(hand_type('23456') == 0)


def parse(file_path: str):
    with open(file_path) as f:
        return [(h, int(b)) for h, b in re.findall(r'(\S+) (\d+)', f.read())]


card_scores = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14,
}

def fn(hand: str):
    ret = [hand_type(hand)]
    for card in hand:
        ret.append(card_scores[card])
    return ret


def fn1(hand:str):
    return (tuple(sorted(Counter(hand).values(), reverse=True)), tuple('23456789TJQKA'.index(c) for c in hand))


def part1(file_path: str):
    hands = parse(file_path)
    sorted_hands = sorted(hands, key=lambda x: fn(x[0]))
    sorted_hands_1 = sorted(hands, key=lambda x: fn1(x[0]))
    assert(sorted_hands == sorted_hands_1)
    winnings = sum(rank * hand[1] for rank, hand in enumerate(sorted_hands, 1))
    return winnings


def fn2(hand: str):
    type_hand = hand
    if 'J' in hand and hand.count('J') < 5:
        type_hand = hand.replace('J', Counter(hand.replace('J', '')).most_common(1)[0][0])
    return (tuple(sorted(Counter(type_hand).values(), reverse=True)), tuple('J23456789TQKA'.index(c) for c in hand))


def part2(file_path: str):
    hands = parse(file_path)
    sorted_hands = sorted(hands, key=lambda x: fn2(x[0]))
    winnings = sum(rank * hand[1] for rank, hand in enumerate(sorted_hands, 1))
    return winnings


assert(part1('test.txt') == 6440)
print(part1('input.txt'))
assert(part2('test.txt') == 5905)
print(part2('input.txt'))

