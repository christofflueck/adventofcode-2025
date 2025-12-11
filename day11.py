from functools import cache
from run_util import run_puzzle


def parse_data(data: str):
    machines = dict()
    for row in data.split("\n"):
        machine, outputs = row.split(": ")
        machines[machine] = outputs.split(" ")
    return machines


def get_paths(machines, src, dst, must_visits=[]):
    @cache
    def dfs(curr, visits):
        if curr in must_visits:
            visits += 1
        if curr == dst:
            return 1 if visits == len(must_visits) else 0
        return sum(dfs(next, visits) for next in machines.get(curr, []))

    return dfs(src, 0)


def part_a(data: str) -> int:
    data = parse_data(data)
    return get_paths(data, "you", "out")


def part_b(data: str) -> int:
    machines = parse_data(data)

    return get_paths(
        machines=machines, src="svr", dst="out", must_visits=["dac", "fft"]
    )


def main():
    examples = [
        (
            """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""",
            5,
            None,
        ),
        (
            """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""",
            None,
            2,
        ),
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
