from run_util import run_puzzle
import bisect


def parse_data(data: str):
    raw_ranges, raw_ids = data.split("\n\n")

    ranges = []

    for x in raw_ranges.split("\n"):
        start, end = map(int, x.split("-"))
        bisect.insort_left(ranges, (start, end))

    index = 1
    while index < len(ranges):
        prev_start, prev_end = ranges[index - 1]
        start, end = ranges[index]

        if (
            start - 1 <= prev_start <= end + 1
            or start - 1 <= prev_end <= end + 1
            or prev_start - 1 <= start <= prev_end + 1
            or prev_start - 1 <= end <= prev_end + 1
        ):
            ranges.pop(index)
            ranges[index - 1] = (min(prev_start, start), max(prev_end, end))
        else:
            index += 1

    return ranges, raw_ids


def part_a(data: str) -> int:
    ranges, raw_ids = parse_data(data)
    ids = set(map(int, raw_ids.split("\n")))

    total = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                total += 1
                break
    return total


def part_b(data: str) -> int:
    ranges, _ = parse_data(data)

    return sum([end - start + 1 for start, end in ranges])


def main():
    examples = [
        (
            """3-5
10-14
16-20
12-18

1
5
8
11
17
32""",
            3,
            14,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
