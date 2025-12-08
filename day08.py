import bisect
from collections import defaultdict
import math
from typing import List, Tuple
from run_util import run_puzzle


def parse_data(data: str) -> List[Tuple[int, int, int]]:
    boxes = []
    for line in data.split("\n"):
        boxes.append(tuple(map(int, line.split(","))))
    return boxes


def part_a(data: str) -> int:
    boxes = parse_data(data)

    distances = []
    required_connections = 10 if len(boxes) == 20 else 1000

    for i, box in enumerate(boxes):
        for other in boxes[i + 1 :]:
            distance = (
                (box[0] - other[0]) ** 2
                + (box[1] - other[1]) ** 2
                + (box[2] - other[2]) ** 2
            )

            bisect.insort_left(
                distances, (distance, box, other), key=lambda x: -1 * x[0]
            )
            distances = distances[-required_connections:]

    junctions = []

    lookup = dict()

    while len(distances) > 0:
        _distance, left, right = distances.pop()

        left_group = lookup.get(left, None)
        right_group = lookup.get(right, None)

        if left_group is None and right_group is None:
            new_junction = set([left, right])
            lookup[left] = new_junction
            lookup[right] = new_junction
            junctions.append(new_junction)
            continue

        if left_group == right_group:
            continue

        if left_group is not None and right_group is not None:
            left_group.update(right_group)
            junctions.remove(right_group)
            for x in right_group:
                lookup[x] = left_group
            continue

        if left_group is not None:
            left_group.add(right)
            lookup[right] = left_group
        else:
            right_group.add(left)
            lookup[left] = right_group

    return math.prod(sorted(map(len, junctions))[-3:])


def part_b(data: str) -> int:
    boxes = parse_data(data)

    distances = []

    for i, box in enumerate(boxes):
        for other in boxes[i + 1 :]:
            distance = (
                (box[0] - other[0]) ** 2
                + (box[1] - other[1]) ** 2
                + (box[2] - other[2]) ** 2
            )

            bisect.insort_left(
                distances, (distance, box, other), key=lambda x: -1 * x[0]
            )

    junctions = []

    lookup = dict()

    last_x_1 = 0
    last_x_2 = 0
    while len(distances) > 0:
        _distance, left, right = distances.pop()

        left_group = lookup.get(left, None)
        right_group = lookup.get(right, None)

        if left_group is None and right_group is None:
            new_junction = set([left, right])
            junctions.append(new_junction)
            lookup[left] = new_junction
            lookup[right] = new_junction
            last_x_1 = left[0]
            last_x_2 = right[0]
            continue

        if left_group == right_group:
            continue

        if left_group is not None and right_group is not None:
            left_group.update(right_group)
            junctions.remove(right_group)
            for x in right_group:
                lookup[x] = left_group
            last_x_1 = left[0]
            last_x_2 = right[0]
            continue

        if left_group is not None:
            left_group.add(right)
            lookup[right] = left_group
            last_x_1 = left[0]
            last_x_2 = right[0]
        else:
            right_group.add(left)
            lookup[left] = right_group
            last_x_1 = left[0]
            last_x_2 = right[0]

    return last_x_1 * last_x_2


def main():
    examples = [
        (
            """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""",
            40,
            25272,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
