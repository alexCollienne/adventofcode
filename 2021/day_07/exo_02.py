if __name__ == "__main__":
    my_file = open("input.txt", "r")
    crabs_position = list(map(int, my_file.readlines()[0].split(",")))
    min_position = min(crabs_position)
    max_position = max(crabs_position)
    moves = {
        position: sum(
            list(map(lambda x: sum(range(abs(x - position) + 1)), crabs_position))
        )
        for position in range(min_position, max_position)
    }
    key_min_move = min(moves, key=moves.get)
    print(moves.get(key_min_move))
