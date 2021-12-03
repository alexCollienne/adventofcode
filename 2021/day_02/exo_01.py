from functools import reduce


def _reducer(totals: list, move: str) -> list:
    if move[:-2] == "forward":
        totals[0] += int(move[-1:])
    elif move[:-2] == "up":
        totals[1] -= int(move[-1:])
    elif move[:-2] == "down":
        totals[1] += int(move[-1:])

    return totals


my_file = open("input.txt", "r")
moves = [move.rstrip() for move in my_file.readlines()]
total_moves = reduce(_reducer, moves, [0, 0])
print(total_moves[0] * total_moves[1])
