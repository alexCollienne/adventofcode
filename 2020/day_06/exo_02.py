from functools import reduce


def _all_members_have_answer(members_answers: list, answer: str) -> bool:
    qt = [1 for ma in members_answers if answer in ma]
    return len(qt) == len(members_answers)


def _count_answers(members_answers: list) -> int:
    return len(
        [
            1
            for i in range(ord("a"), ord("z") + 1)
            if _all_members_have_answer(members_answers, chr(i))
        ]
    )


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    group_answers = "".join(my_file.readlines()).split("\n\n")
    formatted_group_answers = [ga.split("\n") for ga in group_answers]
    right_answers_count = [_count_answers(ga) for ga in formatted_group_answers]
    print(reduce(lambda x, y: x + y, right_answers_count, 0))
