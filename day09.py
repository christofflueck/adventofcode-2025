from run_util import run_puzzle


def parse_data(data: str):
    return [tuple(map(int, x.split(","))) for x in data.split("\n")]


def part_a(data: str) -> int:
    data = parse_data(data)
    count_corners = len(data)

    max_area = 0
    for i in range(count_corners):
        x1, y1 = data[i]
        for j in range(i, count_corners):
            x2, y2 = data[j]

            area = abs((x1 - x2 + 1) * (y1 - y2 + 1))
            max_area = max(max_area, area)

    return max_area


def part_b(data: str) -> int:
    data = parse_data(data)
    return 0


def main():
    examples = [
        (
            """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""",
            50,
            1,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
