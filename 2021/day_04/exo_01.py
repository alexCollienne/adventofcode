import numpy as np


def _get_cards(cards_lines: list) -> list[np]:
    clean_cards_lines = [cl for cl in cards_lines if cl != ""]
    cards = [clean_cards_lines[slice(i, i + 5)] for i in range(0, len(cards_lines), 5)]
    return [
        np.array([row.strip().replace("  ", " ").split(" ") for row in card], int)
        for card in cards
    ]


def _find_number_in_cards(cards: list[np.array], number_to_find: int):
    for card in cards:
        card[card == number_to_find] = 0
        for i in range(card.shape[0]):
            if np.all(card[i] == 0) or np.all(card[:, i] == 0):
                _compute_result(card, number_to_find)
                return


def _compute_result(winning_card: np.array, last_number: int):
    print(np.sum(winning_card) * last_number)


my_file = open("input.txt", "r")
lines = [l.rstrip() for l in my_file.readlines()]
bingo_numbers = [int(l) for l in lines.pop(0).split(",")]
bingo_cards = _get_cards(lines)
[_find_number_in_cards(bingo_cards, bingo_number) for bingo_number in bingo_numbers]
