from functools import reduce


def _is_ok(total: int, preamble_numbers: list[int]) -> bool:
    totals_available = [
        i + j
        for idx_i, i in enumerate(preamble_numbers)
        for idx_j, j in enumerate(preamble_numbers)
        if idx_i != idx_j
    ]

    return total in totals_available


def _get_target_number(numbers: list) -> tuple[int, int]:
    preamble_numbers = [numbers[i] for i in range(25)]
    for index, number in enumerate(numbers[25:]):
        if not _is_ok(number, preamble_numbers):
            return (index + 25), number

        preamble_numbers.pop(0)
        preamble_numbers.append(number)


def _get_following_numbers(target: int, numbers: list) -> list:
    for i in range(2, limit):
        for j in range(limit - i):
            offset = j + i
            extracted_numbers = numbers[j:offset]
            total = reduce(lambda x, y: x + y, extracted_numbers)

            if total == target:
                return extracted_numbers


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    numbers = [int(line.rstrip()) for line in my_file.readlines()]
    limit, targeted_number = _get_target_number(numbers)
    following_numbers = _get_following_numbers(targeted_number, numbers[:limit])
    print(max(following_numbers) + min(following_numbers))
