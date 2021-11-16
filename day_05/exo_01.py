from functools import reduce


def _get_seat_id(seat_code: str) -> int:
    row_moves = seat_code[:7]
    range_moves = seat_code[7:]
    seat_row = reduce(_reducer, row_moves, (0, 127))
    seat_range = reduce(_reducer, range_moves, (0, 7))
    return seat_row[0] * 8 + seat_range[0]


def _reducer(place: tuple, move: str) -> tuple:
    new = int(((place[1] - place[0]) - 1) / 2)
    if move in ["F", "L"]:
        return (place[0], place[1] - new - 1)
    elif move in ["B", "R"]:
        return (place[0] + new + 1, place[1])

    return place


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    lines = my_file.readlines()
    seats_id = sorted([_get_seat_id(l) for l in lines], reverse=True)
    print(seats_id[0])
