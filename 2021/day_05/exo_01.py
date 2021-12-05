from functools import reduce

import numpy as np


def _get_moves(lines) -> list[list[list[int, int]]]:
    all_lines = [
        [
            list(map(int, l.split(" -> ")[0].split(","))),
            list(map(int, l.split(" -> ")[1].split(","))),
        ]
        for l in lines
    ]
    return [l for l in all_lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]


def _get_max_number(moves: list[list[list[int, int]]]) -> int:
    return max([p for move in moves for c in move for p in c])


def _reducer(matrice: np.array, move: list[list[int, int]]):
    if move[0][0] == move[1][0]:
        x = move[0][0]
        for y in range(min(move[0][1], move[1][1]), max(move[0][1], move[1][1]) + 1):
            passages = matrice.item((x, y)) + 1
            matrice.itemset((x, y), passages)
    elif move[0][1] == move[1][1]:
        y = move[0][1]
        for x in range(min(move[0][0], move[1][0]), max(move[0][0], move[1][0]) + 1):
            passages = matrice.item((x, y)) + 1
            matrice.itemset((x, y), passages)

    return matrice


my_file = open("input.txt", "r")
lines = [l.rstrip() for l in my_file.readlines()]
moves = _get_moves(lines)
max_number = _get_max_number(moves) + 1
reduced = reduce(_reducer, moves, np.full((max_number, max_number), 0))
print(sum([1 for p in reduced.flatten() if p >= 2]))
