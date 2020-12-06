def search_number(numbers: list) -> int:
    for first_number in numbers:
        for second_number in numbers:

            searched_number = 2020 - (first_number + second_number)
            if searched_number in numbers:
                return searched_number * first_number * second_number


my_file = open("input.txt", "r")
numbers = []
for line in my_file.readlines():
    numbers.append(int(line))

print(search_number(numbers))
