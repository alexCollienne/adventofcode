from functools import reduce


def _count_answers(group_answer):
    return len([1 for i in range(ord("a"), ord("z") + 1) if chr(i) in group_answer])


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    group_answers = "".join(my_file.readlines()).split("\n\n")
    formatted_group_answers = list(map(lambda x: x.replace("\n", ""), group_answers))
    i = [_count_answers(ga) for ga in formatted_group_answers]
    print(reduce(lambda x, y: x + y, i, 0))
