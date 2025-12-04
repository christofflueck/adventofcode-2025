from collections import defaultdict
from run_util import run_puzzle

ROLL = "@"

DIRECTIONS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def parse_data(data: str):
    rolls = set()
    for y, row in enumerate(data.split("\n")):
        for x, char in enumerate(row):
            if char == ROLL:
                rolls.add((x, y))
    return rolls


def part_a(data: str) -> int:
    rolls = parse_data(data)

    adjacent_rolls = defaultdict(int)

    for x, y in rolls:
        for dx, dy in DIRECTIONS:
            neighbor = (x + dx, y + dy)
            if neighbor in rolls:
                adjacent_rolls[neighbor] += 1

    return sum([1 for roll in rolls if adjacent_rolls[roll] < 4])


def part_b(data: str) -> int:
    rolls = parse_data(data)
    removed_rolls = 0

    adjacent_rolls = defaultdict(int)

    for x, y in rolls:
        for dx, dy in DIRECTIONS:
            neighbor = (x + dx, y + dy)
            if neighbor in rolls:
                adjacent_rolls[neighbor] += 1

    removable_rolls = [roll for roll in rolls if adjacent_rolls[roll] < 4]

    while len(removable_rolls) > 0:

        while len(removable_rolls) > 0:
            x, y = removable_rolls.pop()
            for dx, dy in DIRECTIONS:
                neighbor = (x + dx, y + dy)
                if neighbor in rolls:
                    adjacent_rolls[neighbor] -= 1
            rolls.remove((x, y))
            removed_rolls += 1

        removable_rolls = [roll for roll in rolls if adjacent_rolls[roll] < 4]

    return removed_rolls


def main():
    examples = [
        (
            """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""",
            13,
            43,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
