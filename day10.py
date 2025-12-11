from run_util import run_puzzle


def parse_data(data: str):
    for machine in data.splitlines():
        machine_end = machine.find("]")
        toggles_start = machine_end + 3
        joltages_start = machine.find("{")
        toggles_end = joltages_start - 2
        lights = [char == "#" for char in machine[1 : machine.find("]")]]
        toggles = [
            [int(x) for x in x.split(",")]
            for x in machine[toggles_start:toggles_end].split(") (")
        ]
        joltages = [int(x) for x in machine[joltages_start + 1 : -1].split(",")]
        yield lights, toggles, joltages


def part_a(data: str) -> int:
    data = list(parse_data(data))
    print(data)
    return 0


def part_b(data: str) -> int:
    data = parse_data(data)
    return 0


def main():
    examples = [
        (
            """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""",
            7,
            1,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
