from collections import defaultdict

from run_util import run_puzzle


def parse_data(data: str):
    start = None
    splitters = set()

    rows = data.split('\n')
    max_x = len(rows[0])
    max_y = len(rows)

    for y in range(max_y):
        for x in range(max_x):
            cell = rows[y][x]
            match cell:
                case 'S':
                    start = (x, y)
                case '^':
                    splitters.add((x, y))

    return start, splitters, max_x, max_y


def part_a(data: str) -> int:
    start, splitters, max_x, max_y = parse_data(data)
    beams = {start[0]}
    splits = 0
    for y in range(0, max_y, 2):
        next_beams = set()
        for x in beams:
            if (x,y) in splitters:
                next_beams.add(x + 1)
                next_beams.add(x - 1)
                splits += 1
            else:
                next_beams.add(x)
        beams = next_beams

    return splits


def part_b(data: str) -> int:
    start, splitters, max_x, max_y = parse_data(data)
    beams = {start[0]: 1}
    for y in range(0, max_y, 2):
        next_beams = defaultdict(int)
        for x in beams:
            if (x,y) in splitters:
                next_beams[x + 1] += beams[x]
                next_beams[x - 1] += beams[x]
            else:
                next_beams[x] += beams[x]
        beams = next_beams


    return sum(beams.values())


def main():
    examples = [
        (""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""", 21, 40)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
