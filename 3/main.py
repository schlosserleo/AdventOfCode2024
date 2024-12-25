import re


def parser(filename: str) -> str:
    line: str
    result: str = str()
    with open(filename, "r") as input:
        for line in input:
            result += line

    return result


def mulitply(mul_str: str | None) -> int:
    if mul_str is None:
        return 0

    numbers = list()

    for match in re.findall(r"[0-9]+", mul_str):
        numbers.append(int(match))

    return numbers[0] * numbers[1]


def solve_part_one(input: str) -> int:
    result: int = 0
    matches: list[str | None]

    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)
    for match in matches:
        result += mulitply(match)

    return result


def solve_part_two(input: str) -> int:
    result: int = 0
    section_pattern = re.compile(r"(?:do\(\)|\A)(?:.|\n)*?don't\(\)", re.MULTILINE)
    mul_pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    do_sections = re.findall(section_pattern, input)
    for do_section in do_sections:
        matches = re.findall(mul_pattern, do_section)
        for match in matches:
            result += mulitply(match)

    return result


def solve(input: str) -> None:
    print("Part one:")
    print(solve_part_one(input))
    print("Part two")
    print(solve_part_two(input))


if __name__ == "__main__":
    input = parser("input.txt")
    solve(input)
