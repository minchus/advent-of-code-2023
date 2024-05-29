import re


def parse(file_path: str):
    with open(file_path) as f:
        lines = f.readlines()

    maps = []
    ranges = []

    for line in lines:
        if 0 == len(line.strip()):
            pass
        elif 'seeds' in line:
            matches = re.findall(r'\b\d+\b', line)
            seeds = [int(match) for match in matches]
        elif 'map' in line:
            maps.append(ranges)
            ranges = []
        else:
            matches = re.findall(r'\b\d+\b', line)
            r = [int(match) for match in matches]
            ranges.append(r)

    maps.append(ranges)
    maps = [x for x in maps if len(x) > 0]

    return seeds, maps


def part1(file_path: str):
    seeds, maps = parse(file_path)
    # print(f'seeds={seeds}')
    # print(f'maps={maps}')

    locations = []
    for s in seeds:
        for ranges in maps:
            for r in ranges:
                dst = r[0]
                src = r[1]
                length = r[2]

                if s >= src and s < src + length:
                    s = dst + (s - src)
                    break

        locations.append(s)

    # print(f'locations={locations}')
    return min(locations)

assert(part1('test.txt') == 35)
print(part1('input.txt'))


def part2(file_path: str):
    with open(file_path) as f:
        puzzle_input = f.read()

    segments = puzzle_input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))
  
    return min_location

assert(part2('test.txt') == 46)
print(part2('input.txt'))


