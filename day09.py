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


def print_debug(corners, start, end):
    max_x = max(x for x, _ in corners)
    max_y = max(y for _, y in corners)
    highlighted = set()
    if start is not None and end is not None:
        x1, y1 = start
        x2, y2 = end
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                highlighted.add((x, y))

    for y in range(max_y + 2):
        for x in range(max_x + 3):

            print(
                f"{'#' if (x, y) in corners else 'X' if (x, y) in highlighted else '.' }",
                end="",
            )

        print()


def part_b(corners: str) -> int:
    corners = parse_data(corners)
    count_corners = len(corners)

    horizontals = []
    verticals = []

    for i in range(count_corners):
        x1, y1 = corners[i]
        for j in range(i + 1, count_corners):
            x2, y2 = corners[j]

            if x1 == x2:
                horizontals.append((x1, min(y1, y2), max(y1, y2)))
                print(
                    f"Line {corners[i]} -> {corners[j]}, {(x1, min(y1, y2), max(y1, y2))}"
                )
                continue
            if y1 == y2:
                verticals.append((y1, min(x1, x2), max(x1, x2)))
                print(
                    f"Line {corners[i]} -> {corners[j]}, {(y1, min(x1, x2), max(x1, x2))}"
                )
                continue

    max_area = 0
    for i in range(count_corners):
        x1, y1 = corners[i]
        for j in range(i + 1, count_corners):
            x2, y2 = corners[j]

            low_x = min(x1, x2)
            high_x = max(x1, x2)

            low_y = min(y1, y2)
            high_y = max(y1, y2)

            area = (high_x - low_x + 1) * (high_y - low_y + 1)

            print(
                f"                   -------------- Testing {corners[i]} and {corners[j]}"
            )
            print_debug(corners, corners[i], corners[j])

            if area <= max_area:
                print("Is Smaller")
                continue
            print("Is Bigger")

            crosses_line = False
            for line_x, line_start, line_end in horizontals:
                if (
                    (line_start < low_y < line_end or line_start < high_y < line_end)
                    and not line_start < low_y < high_y < line_end
                    and low_x <= line_x <= high_x
                ):
                    print(
                        f"Line Crossing with horizontal f{(line_x, line_start)} -> {(line_x, line_end) }"
                    )
                    print_debug(corners, (line_x, line_start), (line_x, line_end))
                    crosses_line = True
                    break

            if crosses_line:
                continue

            for line_y, line_start, line_end in verticals:
                if (
                    (line_start < low_x < line_end or line_start < high_x < line_end)
                    and not line_start < low_x < high_x < line_end
                    and low_y <= line_y <= high_y
                ):
                    print(
                        f"Line Crossing with vertical f{(line_start, line_y)} -> {(line_end, line_y) }"
                    )
                    print_debug(corners, (line_start, line_y), (line_end, line_y))
                    crosses_line = True
                    break

            if crosses_line:
                continue

            print(f"Found new best: {area}")
            max_area = area

    return max_area


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
            24,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
