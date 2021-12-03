import typing
from functools import reduce


def _format_rules(lines: list) -> dict:
    def _get_key_bag(child_bag) -> str:
        return child_bag[2:].rstrip(".").replace(" bags", "").replace(" bag", "")

    def _get_child_bags(child_bags: str) -> dict:
        if child_bags == "no other bags.\n":
            return {}

        list_child_bags = child_bags.rstrip(".\n").split(", ")
        return {
            _get_key_bag(child_bag): int(child_bag[:1]) for child_bag in list_child_bags
        }

    return {
        line.split(" bags contain ")[0]: _get_child_bags(
            line.split(" bags contain ")[1]
        )
        for line in lines
    }


def _get_bags(bag: str) -> list:
    bag_content = bags_content[bag]
    return list(
        qt if len(bags_content[bag]) == 0 else [qt, _get_bags(bag)]
        for bag, qt in bag_content.items()
    )


def _reducer(total: int, item: typing.Union[list, int]) -> int:
    to_add = 0
    if isinstance(item, int):
        to_add = item
    elif isinstance(item[0], int):
        if any(i for i in item[1] if isinstance(i, list)):
            to_add = (item[0] * reduce(_reducer, item[1], 0)) + item[0]
        elif isinstance(item[1], list) and all(
            i for i in item[1] if isinstance(i, int)
        ):
            to_add = reduce(lambda x, y: x + (item[0] * y), item[1], 0) + item[0]
    elif isinstance(item, list):
        to_add = reduce(_reducer, item, 0)

    return total + to_add


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    bags_content = _format_rules(my_file.readlines())
    shiny_gold_bag_content = bags_content["shiny gold"]
    qt_list = [[qt, _get_bags(bag)] for bag, qt in shiny_gold_bag_content.items()]
    # qt_list = [[2, [[2, [[2, [[2, [[2, [2]]]]]]]]]]]
    total_bags_count = reduce(_reducer, qt_list, 0)

    print(total_bags_count)
