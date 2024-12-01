def parser(filename: str) -> list[list[int]]:
    line: str
    list_one: list[int] = list()
    list_two: list[int] = list()
    with open(filename, "r") as input:
        for line in input:
            split_line: list[str] = line.split()
            list_one.append(int(split_line[0]))
            list_two.append(int(split_line[1]))

    return [list_one, list_two]


def solve(list_one: list[int], list_two: list[int]) -> None:
    print("Part one:")
    print(solve_part_one(list_one, list_two))
    print("\nPart two:")
    print(solve_part_two(list_one, list_two))


def solve_part_one(list_one: list[int], list_two: list[int]) -> int:
    result: int = 0

    list_one.sort()
    list_two.sort()

    for i, x in enumerate(list_one):
        result += abs(x - list_two[i])

    return result


def solve_part_two(list_one: list[int], list_two: list[int]) -> int:
    result: int = 0
    list_one_no_double_entries: list[int] = list()

    for i, x in enumerate(list_one):
        if x not in list_one_no_double_entries:
            list_one_no_double_entries.append(x)

    for i, x in enumerate(list_one_no_double_entries):
        result += x * list_one.count(x) * list_two.count(x)

    return result


if __name__ == "__main__":
    parsed_input: list[list[int]] = parser("input.txt")
    solve(parsed_input[0], parsed_input[1])
