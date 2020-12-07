import math


def count_trees(map: list, base_counter: int) -> int:
    counter = 0
    total_trees = 0
    line_length = len(map[0])
    for line in map:
        counter += base_counter
        round_base = math.floor(counter / line_length)
        key = counter - (round_base * line_length)
        total_trees += line[key]
    return total_trees


my_file = open("input.txt", "r")
lines = my_file.readlines()

map = []
for line in lines:
    formatted_line = [0 if c == "." else 1 for c in line.rstrip("\n")]
    map.append(formatted_line)

map.pop(0)
total_trees = count_trees(map, 3)

print(total_trees)
