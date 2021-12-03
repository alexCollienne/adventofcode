if __name__ == "__main__":
    my_file = open("input.txt", "r")
    adapters = sorted([int(line.rstrip()) for line in my_file.readlines()])
    previous_adapter = 0
    three = 1
    one = 0
    for adapter in adapters:
        if adapter - previous_adapter == 3:
            three += 1
        elif adapter - previous_adapter == 1:
            one += 1
        previous_adapter = adapter

    print(one * three)
