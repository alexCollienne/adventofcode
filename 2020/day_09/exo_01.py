def _is_ok(total: int, preamble_numbers: list[int]) -> bool:
    totals_available = [
        i + j
        for idx_i, i in enumerate(preamble_numbers)
        for idx_j, j in enumerate(preamble_numbers)
    ]

    return total in totals_available


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    numbers = [int(line.rstrip()) for line in my_file.readlines()]
    preamble_numbers = [numbers.pop(0) for _ in range(25)]

    for number in numbers:
        if not _is_ok(number, preamble_numbers):
            print(number)
            break

        preamble_numbers.pop(0)
        preamble_numbers.append(number)
