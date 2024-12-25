def parser(filename: str) -> list[list[int]]:
    line: str
    parsed_numbers: list[list[int]] = list()
    with open(filename, "r") as input:
        for line in input:
            split_line: list[str] = line.split()
            parsed_numbers.append(list(map(int, split_line)))

    return parsed_numbers


def calc_diff(a: int, b: int) -> int:
    return a - b


def same_sign(a: int, b: int) -> bool:
    if a < 0:
        return b < 0

    return b > 0


def check_if_diff_valid(direction: int, current_diff: int) -> bool:
    if abs(current_diff) < 1 or abs(current_diff) > 3:
        return False

    if not same_sign(current_diff, direction):
        return False

    return True


def check_line(line: list[int]):
    current_diff: int
    direction: int

    direction = calc_diff(line[0], line[len(line) - 1])

    for i in range(0, len(line) - 1):
        current_diff = calc_diff(line[i], line[i + 1])

        if not check_if_diff_valid(direction, current_diff):
            return False

    return True


def solve_part_one(input: list[list[int]]):
    result: int = 0
    for line in input:
        if check_line(line):
            result += 1

    return result


def solve_part_two(input: list[list[int]]):
    result: int = 0
    line_copy: list[int]
    for line in input:
        for i in range(0, len(line)):
            line_copy = list(line)
            line_copy.pop(i)

            if check_line(line_copy):
                result += 1
                break
    return result


def solve(input: list[list[int]]) -> None:
    print("Part one:")
    print(solve_part_one(input))
    print("Part two:")
    print(solve_part_two(input))


if __name__ == "__main__":
    parsed_numbers: list[list[int]] = parser("input.txt")
    solve(parsed_numbers)
