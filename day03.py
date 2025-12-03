from collections import defaultdict
from run_util import run_puzzle


def parse_data(data: str):
    return [[int(battery) for battery in bank] for bank in data.split("\n")]


def part_a(data: str) -> int:
    banks = parse_data(data)

    num_batteries = 2
    total_jolts = 0

    for bank in banks:
        used_batteries = set()
        jolts = ""
        start = 0
        for i in range(num_batteries):
            highest = None
            subbank = bank[start : len(bank) - num_batteries + i + 1]
            for batteryIndex, battery in enumerate(subbank):
                if batteryIndex + start in used_batteries:
                    continue
                if highest is None:
                    highest = batteryIndex + start
                    continue
                if battery > bank[highest]:
                    highest = batteryIndex + start
            start = highest + 1
            used_batteries.add(highest)
            jolts += str(bank[highest])

        total_jolts += int(jolts)

    return total_jolts


def part_b(data: str) -> int:
    banks = parse_data(data)

    num_batteries = 12
    total_jolts = 0

    for bank in banks:
        used_batteries = set()
        jolts = ""
        start = 0
        for i in range(num_batteries):
            highest = None
            subbank = bank[start : len(bank) - num_batteries + i + 1]
            for batteryIndex, battery in enumerate(subbank):
                if batteryIndex + start in used_batteries:
                    continue
                if highest is None:
                    highest = batteryIndex + start
                    continue
                if battery > bank[highest]:
                    highest = batteryIndex + start
            start = highest + 1
            used_batteries.add(highest)
            jolts += str(bank[highest])

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
