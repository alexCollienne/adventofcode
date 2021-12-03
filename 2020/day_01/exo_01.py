def search_number(numbers: list) -> int:
    for number in numbers:
        searched_number = 2020 - number
        if searched_number in numbers:
            return searched_number * number


my_file = open("input.txt", "r")
numbers = []
for line in my_file.readlines():
    numbers.append(int(line))

print(search_number(numbers))
