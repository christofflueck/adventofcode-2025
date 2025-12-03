from collections import defaultdict
from run_util import run_puzzle


def parse_data(data: str):
    return [[int(battery) for battery in bank] for bank in data.split("\n")]


def part_a(data: str) -> int:
    banks = parse_data(data)

    num_batteries = 2

    return get_jolts(banks, num_batteries)


def part_b(data: str) -> int:
    banks = parse_data(data)

    num_batteries = 12
    return get_jolts(banks, num_batteries)


def get_jolts(banks, num_batteries):
    total_jolts = 0
    for bank in banks:
        jolts = 0
        start = 0
        max_end = len(bank) - num_batteries + 1
        for i in range(num_batteries):
            subbank = bank[start: max_end + i ]
            highest = start + max(range(len(subbank)), key=subbank.__getitem__)
            start = highest + 1
            jolts += bank[highest] * 10**(num_batteries - i - 1)

        total_jolts += int(jolts)
    return total_jolts


def main():
    examples = [
        (
            """987654321111111
811111111111119
234234234234278
818181911112111""",
            357,
            3121910778619,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
