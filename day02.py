from typing import List, Tuple
from run_util import run_puzzle


def parse_data(data: str) -> List[Tuple[int, int, str, str]]:
    ranges = []
    for pair_str in data.split(","):
        start, end = pair_str.split("-")
        ranges.append((int(start), int(end), len(start), len(end)))

    return ranges


def part_a(data: str) -> int:
    data = parse_data(data)

    agg = 0
    len_segment = 2
    for start, end, len_start, len_end in data:
        absolute_min = start // (
            10
            ** (len_start // len_segment + (1 if len_start % len_segment != 0 else 0))
        )
        absolute_max = end // (
            10 ** (len_end // len_segment - (1 if len_end % 2 != 0 else 0))
        )

        for curr_len in range(len_start, len_end + 1):
            if curr_len % len_segment != 0:
                continue
            half = curr_len // len_segment

            segment_start = max(absolute_min, int("1" + "0" * (half - 1)))
            segment_end = min(absolute_max, int("9" * half))

            for i in range(segment_start, segment_end + 1):
                curr = int(str(i) * len_segment)
                if start <= curr <= end:

                    agg += curr

    return agg


def part_b(data: str) -> int:
    data = parse_data(data)

    agg = 0

    for start, end, len_start, len_end in data:
        found = set()

        for num_segments in range(2, len_end + 1):
            len_segment = None
            for i in range(1, len_end + 1):
                if len_start <= (i * num_segments) <= len_end:
                    len_segment = i
                    break
            if len_segment is None:
                continue

            for curr_len in range(len_start, len_end + 1):
                if curr_len % num_segments != 0:
                    continue
                half = curr_len // num_segments

                segment_start = int("1" + "0" * (half - 1))
                segment_end = int("9" * half)

                for i in range(segment_start, segment_end + 1):
                    curr = int(str(i) * num_segments)
                    if start <= curr <= end:
                        found.add(curr)
        agg += sum(found)
    return agg


def main():
    examples = [
        (
            """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""",
            1227775554,
            4174379265,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
