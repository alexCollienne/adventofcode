import typing
from functools import reduce


def _reducer(x: dict, y: int) -> dict:
    x["increased"] += 1 if x["previous_depth"] and y > x["previous_depth"] else 0
    x["previous_depth"] = y
    return x


my_file = open("input.txt", "r")
depths = [int(line.rstrip()) for line in my_file.readlines()]
summary = reduce(_reducer, depths, {"previous_depth": None, "increased": 0})
print(summary.get("increased", 0))
