import typing
from functools import reduce


def _format_rules(lines: list):
    def _get_child_bags(child_bags: str) -> list:
        list_child_bags = child_bags.rstrip(".\n").split(", ")
        return [
            child_bag[2:].replace(" bags", "").replace(" bag", "")
            for child_bag in list_child_bags
        ]

    return {
        line.split(" bags contain ")[0]: _get_child_bags(
            line.split(" bags contain ")[1]
        )
        for line in lines
    }


def _reducer(bags: list[str], bag_rule: tuple[str, list]) -> list[str]:
    valid_bags = [bag_rule[0] for bag in bags if bag in bag_rule[1]]
    return [*bags, *valid_bags]


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    bags_rules = _format_rules(my_file.readlines())
    current_bags = ["shiny gold"]
    bags_qt = 0
    i = 1
    while len(current_bags) != bags_qt:
        print(f"loop {i}")
        new_bags = [
            parent_bag
            for parent_bag, child_bags in bags_rules.items()
            for child_bag in child_bags
            if child_bag in current_bags
        ]
        bags_qt = len(current_bags)
        current_bags = list(dict.fromkeys([*new_bags, *current_bags]))
        i += 1

    print(len(current_bags) - 1)
