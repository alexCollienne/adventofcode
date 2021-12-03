from functools import reduce


def _reducer(totals: dict, move: str) -> dict:
    if move[:-2] == "forward":
        totals["h"] += int(move[-1:])
        totals["d"] += totals["aim"] * int(move[-1:])
    elif move[:-2] == "up":
        totals["aim"] -= int(move[-1:])
    elif move[:-2] == "down":
        totals["aim"] += int(move[-1:])

    return totals


my_file = open("input.txt", "r")
moves = [move.rstrip() for move in my_file.readlines()]
total_moves = reduce(_reducer, moves, {"h": 0, "d": 0, "aim": 0})
print(total_moves["h"] * total_moves["d"])
