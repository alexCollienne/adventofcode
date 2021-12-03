import typing
from functools import reduce


def _reducer(x: dict, y: int) -> dict:
    x["increased"] += 1 if x["previous_depth"] and y > x["previous_depth"] else 0
    x["previous_depth"] = y
    return x


my_file = open("input.txt", "r")
depths = [int(line.rstrip()) for line in my_file.readlines()]


def _compute_depths(depths: list[int]) -> list[int]:
    return [
        sum([d, depths[i + 1], depths[i + 2]])
        for i, d in enumerate(depths)
        if i <= len(depths) - 3
    ]


computed_depths = _compute_depths(depths)
summary = reduce(_reducer, computed_depths, {"previous_depth": None, "increased": 0})
print(summary.get("increased", 0))
