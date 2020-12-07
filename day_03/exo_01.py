import math


def count_trees(map: list, base_counter: int) -> int:
    counter = 0
    total_trees = 0
    line_length = len(map[0])
    for line in map:
        counter += base_counter
        round_base = math.floor(counter / line_length)
        key = counter - (round_base * line_length)
        total_trees += 1 if line[key] == "#" else 0
    return total_trees


if __name__ == '__main__':
    with open("input.txt", "r") as my_file:
        map = my_file.read().splitlines()

    map.pop(0)
    total_trees = count_trees(map, 3)

    print(total_trees)
