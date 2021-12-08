from collections import defaultdict
from functools import reduce


def _reducer(grouped_digits: dict, line_digits: list[str]) -> dict:
    map_len_digit = {2: 1, 4: 4, 3: 7, 7: 8}
    for digit in line_digits:
        len_digit = len(digit)
        if len_digit in map_len_digit:
            grouped_digits[map_len_digit.get(len_digit)] += 1
    return grouped_digits


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    all_digits = list(
        map(
            lambda line: [digit for digit in line.rstrip().split(" | ")[1].split(" ")],
            my_file.readlines(),
        )
    )
    digits_by_length = reduce(_reducer, all_digits, defaultdict(lambda: 0))

    print(
        digits_by_length[1]
        + digits_by_length[4]
        + digits_by_length[7]
        + digits_by_length[8]
    )
