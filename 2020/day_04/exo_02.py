import re


def _birth_year_validation(year: str) -> bool:
    return year.isnumeric() and len(year) == 4 and 1919 < int(year) <= 2002


def _issue_year_validation(year: str) -> bool:
    return year.isnumeric() and len(year) == 4 and 2009 < int(year) <= 2020


def _expiration_year_validation(year: str) -> bool:
    return year.isnumeric() and len(year) == 4 and 2019 < int(year) <= 2030


def _height_validation(height: str) -> bool:
    return ("cm" in height or "in" in height) and (
        ("cm" in height and (149 < int(height.replace("cm", "")) <= 193))
        or ("in" in height and (58 < int(height.replace("in", "")) <= 76))
    )


def _hair_color_validation(color: str) -> bool:
    return bool(re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", color))


def _eye_color_validation(color: str) -> bool:
    return color in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def _passport_id_validation(id: str) -> bool:
    return bool(re.search(r"^(?:[0-9]{9})$", id))


def _line_validation(line: str) -> bool:
    line = line.replace("\n", " ")
    passport = {item.split(":")[0]: item.split(":")[1] for item in line.split()}
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    return (
        set(required_keys).issubset(passport.keys())
        and _birth_year_validation(passport["byr"])
        and _issue_year_validation(passport["iyr"])
        and _expiration_year_validation(passport["eyr"])
        and _height_validation(passport["hgt"])
        and _hair_color_validation(passport["hcl"])
        and _eye_color_validation(passport["ecl"])
        and _passport_id_validation(passport["pid"])
    )


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    lines = "".join(my_file.readlines()).split("\n\n")
    valid_lines = [l for l in lines if _line_validation(l)]
    print(len(valid_lines))
