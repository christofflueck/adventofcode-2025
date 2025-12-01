from run_util import run_puzzle


def parse_data(data: str):
    return [int(x[1:]) * (-1 if x[0] == 'L' else 1) for x in data.split('\n')]


def part_a(data: str) -> int:
    data = parse_data(data)
    curr = 50
    visited_zero = 0
    for distance in data:
        curr += distance
        curr %= 100
        if curr == 0: 
            visited_zero += 1
    return visited_zero


def part_b(data: str) -> int:
    data = parse_data(data)
    curr = 50
    visited_zero = 0
    for distance in data:
        curr += distance
        visited_zero += abs(curr // 100)
        curr %= 100
    return visited_zero


def main():
    examples = [
        ("""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""", 3, 6)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()