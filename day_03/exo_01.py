def password_is_valid(password: str, policy: str) -> bool:
    numbers, letter = policy.split(" ")
    number_min, number_max = numbers.split("-")

    return int(number_max) >= password.count(letter) >= int(number_min)


my_file = open("input.txt", "r")
passwords_with_policy = my_file.readlines()

valid_passwords_count = 0
for password_with_policy in passwords_with_policy:
    policy, password = password_with_policy.split(": ")

    valid_passwords_count += 1 if password_is_valid(password, policy) else 0

print(valid_passwords_count)
