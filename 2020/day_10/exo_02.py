from functools import reduce


def _count_valid_lists(adapters: list) -> int:
    count_group = 0
    previous_adapter = None
    total = 1
    for adapter in adapters:
        if previous_adapter and adapter - previous_adapter == 3 and count_group > 2:
            total *= count_group - 2
            count_group = 0
        elif previous_adapter and adapter - previous_adapter == 3:
            count_group = 0

        count_group += 1
        previous_adapter = adapter

    return total


def _reducer(groups: list, adapter: int) -> list:
    if len(groups):
        last_group = groups[-1]
        if adapter - last_group[-1] == 3:
            groups.append([adapter])
        else:
            last_group.append(adapter)
    else:
        groups.append([adapter])

    return groups


def _computer(x: dict, group: list) -> dict:
    if len(group) == 4:
        x["x"] += 1

    if len(group) == 5:
        x["y"] += 1

    if len(group) == 6:
        x["z"] += 1

    return x


def factorielle(n):
    if n == 0:
        return 0
    else:
        F = 1
        for k in range(2, n + 1):
            F = F * k

        return F


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    adapters = sorted([int(line.rstrip()) for line in my_file.readlines()])
    adapters.insert(0, 0)
    # adapters = [0, 1, 2, 3, 4, 7, 8, 9, 10]

    reduced = reduce(_reducer, adapters, [])
    computed_groups = reduce(_computer, reduced, {"x": 0, "y": 0, "z": 0})

    print(2 ** computed_groups["x"] * 3 * computed_groups["y"])
