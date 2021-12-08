if __name__ == "__main__":
    my_file = open("input.txt", "r")
    lanternfishes = list(map(int, my_file.readlines()[0].split(",")))
    for day in range(80):
        next_children_quantity = lanternfishes.count(0)
        lanternfishes = list(map(lambda x: x - 1 if x > 0 else 6, lanternfishes))
        lanternfishes += [8 for _ in range(next_children_quantity)]

    print(len(lanternfishes))
