from collections import defaultdict

def parse(file_path: str):
    with open(file_path) as f:
        lines = f.readlines()

    game_list = []
    for line in lines:
        draws = line.split(':')[-1].strip()
        draw_list = []
        for d in draws.split(';'):
            d = d.strip()
            cube_counts = d.split(',')

            draw_dict = defaultdict(int)
            for c in cube_counts:
                count = int(c.split()[0])
                color = c.split()[-1]
                # print(f'{count}: {color}')
                draw_dict[color] = count
            draw_list.append(draw_dict)

        game_list.append(draw_list)

    return game_list


def part1(game_list: list):
    def draw_possible(input_draw):
        available = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }
        for color, count in input_draw.items():
            if available[color] < count:
                return False
        return True

    game_sum = 0
    for game_number, game in enumerate(game_list, 1):
        for draw in game:
            # print(f'Game {game_number}: {draw} {"possible" if draw_possible(draw) else "impossible"}')
            if not draw_possible(draw):
                break
        else:
            game_sum += game_number

    return game_sum


def part2(game_list: list):
    power_sum = 0

    for game in game_list:
        max_red = max([draw['red'] for draw in game])
        max_green = max([draw['green'] for draw in game])
        max_blue = max([draw['blue'] for draw in game])

        # print(f'max_red={max_red} max_green={max_green} max_blue={max_blue}')
        power = max_red * max_green * max_blue
        power_sum += power
    return power_sum


game_list = parse('test.txt')
assert part1(game_list) == 8
assert part2(game_list) == 2286

game_list = parse('input.txt')
print(f'part1={part1(game_list)}')
print(f'part2={part2(game_list)}')




