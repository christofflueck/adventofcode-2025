import math

from run_util import run_puzzle


def parse_data(data: str):
    problems = []
    rows = data.split('\n')
    for y, row in enumerate(rows):
        cols = row.split()
        if len(problems) == 0:
            for _ in range(len(cols)):
                problems.append([])
        for x, cell in enumerate(cols):
            if y == len(rows) - 1:
                problems[x].append(cell)
            else:
                problems[x].append(int(cell))
    return problems


def part_a(data: str) -> int:
    data = parse_data(data)
    total = 0
    for problem in data:
        op = problem.pop()
        match op:
            case '*':
                total += math.prod(problem)
            case '+':
                total += sum(problem)

    return total


def part_b(data: str) -> int:
    problems = []
    rows = data.split('\n')
    curr_problem = []
    for x in range(len(rows[0])):
        if rows[-1][x] != ' ':
            curr_problem.append(rows[-1][x])

        num = "".join([rows[y][x] for y in range(len(rows) - 1)]).strip()
        if len(num) > 0:
            curr_problem.append(int(num))
        else:
            problems.append(curr_problem)
            curr_problem = []
    problems.append(curr_problem)

    total = 0
    for problem in problems:
        op = problem.pop(0)
        match op:
            case '*':
                total += math.prod(problem)
            case '+':
                total += sum(problem)
    return total


def main():
    examples = [
        ("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """, 4277556, 3263827)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
