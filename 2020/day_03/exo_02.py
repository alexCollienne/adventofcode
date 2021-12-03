import math


def count_trees(map: list, base_counter: int) -> int:
    counter = 0
    total_trees = 0
    line_length = len(map[0])
    for line in map:
        counter += base_counter
        round_base = math.floor(counter / line_length)
        key = counter - (round_base * line_length)
        total_trees += 0 if line[key] == "." else 1
    return total_trees


def prepare_map(map: list, lines_count: int) -> list:
    copy_map = map.copy()
    for idx in reversed(range(len(map))):
        if idx % lines_count == 0:
            copy_map.pop(idx)

    return copy_map


my_file = open("input.txt", "r")
lines = my_file.readlines()

map = []
for line in lines:
    map.append(line.rstrip("\n"))

map.pop(0)
print(
    count_trees(map, 1)
    * count_trees(map, 3)
    * count_trees(map, 5)
    * count_trees(map, 7)
    * count_trees(prepare_map(map, 2), 1)
)
