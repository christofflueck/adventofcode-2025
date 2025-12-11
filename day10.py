from z3 import Int, Solver, Sum, sat, Optimize

from run_util import run_puzzle
from collections import deque


def parse_data(data: str):
    for machine in data.splitlines():
        machine_end = machine.find("]")
        toggles_start = machine_end + 3
        joltages_start = machine.find("{")
        toggles_end = joltages_start - 2
        lights = [1 if char == "#" else 0 for char in machine[1: machine.find("]")]]
        toggles = [
            [int(x) for x in x.split(",")]
            for x in machine[toggles_start:toggles_end].split(") (")
        ]
        toggles = [[1 if i in t else 0 for i in range(len(lights))] for t in toggles]
        joltages = [int(x) for x in machine[joltages_start + 1: -1].split(",")]
        yield lights, toggles, joltages


def part_a(data: str) -> int:
    data = list(parse_data(data))

    total_clicks = 0
    for lights, toggles, _ in data:
        queue = deque([
            ([0 for _ in range(len(lights))], i, 1)
            for i in range(len(toggles))
        ])

        while queue:
            state, toggle_index, clicks = queue.popleft()
            state = [(state[i] + toggles[toggle_index][i]) % 2 for i in range(len(state))]
            if state == lights:
                total_clicks += clicks
                break

            for i in range(len(toggles)):
                if i != toggle_index:
                    queue.append((state, i, clicks + 1))

    return total_clicks


def part_b(data: str) -> int:
    data = list(parse_data(data))

    total_clicks = 0
    for _, toggles, joltage in data:
        s = Optimize()
        toggle_clicks = [Int(f"t{i}") for i in range(len(toggles))]

        for t in toggle_clicks:
            s.add(t >= 0)

        for joltage_index, j in enumerate(joltage):
            s.add(j == Sum([toggle_clicks[i] * toggles[i][joltage_index] for i in range(len(toggles))]))

        s.minimize(Sum(toggle_clicks))

        if s.check() == sat:
            m = s.model()
            total_clicks += sum(m[t].as_long() for t in toggle_clicks)
        else:
            print("Warning: A machine has no solution!")

    return total_clicks


def main():
    examples = [
        (
            """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""",
            7,
            33,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
