import re


def parser(filename: str) -> list[str]:
    result: list[str] = list()
    with open(filename, "r") as input:
        for line in input:
            result.append(line)

    return result


def horizontal_flip(input: list[str]) -> list[str]:
    result: list[str] = list()
    for i in range(len(input)):
        result.append("")

    for line in input:
        for i, x in enumerate(line):
            result[i - 1] += x

    return result


def solve_part_one(input: list[str]) -> int:
    result: int = 0
    forward_lines = input
    backward_lines = reversed(input)
    downwards_lines = horizontal_flip(input)
    upwards_lines = reversed(downwards_lines)

    diagnoal_lines = list()
    
    for i in range(0, len(forward_lines)):
        for j in forward_lines:
            diagnoal_lines.append(len(j[i])

    all_orientations = [forward_lines, backward_lines, downwards_lines, upwards_lines]
    pattern = re.compile("XMAS")
    for orientation in all_orientations:
        for line in orientation:
            result += len(re.findall(pattern, line))

    return result


def solve(input: list[str]) -> None:
    print("Part one:")
    print(solve_part_one(input))


if __name__ == "__main__":
    input: list[str] = parser("input.txt")
    solve(input)
