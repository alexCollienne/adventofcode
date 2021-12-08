from collections import defaultdict
from functools import reduce


def _reducer(lanternfishes_by_day: dict, lanternfish: int) -> dict:
    lanternfishes_by_day[lanternfish] += 1
    return lanternfishes_by_day


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    lanternfishes = list(map(int, my_file.readlines()[0].split(",")))
    default_lanternfishes_by_day = defaultdict(lambda: 0)
    lanternfishes_by_day = reduce(_reducer, lanternfishes, default_lanternfishes_by_day)
    for day in range(2560):
        print(f"Day {day}")
        lanternfishes_by_day = {
            day - 1: val for day, val in lanternfishes_by_day.items()
        }
        if 6 not in lanternfishes_by_day:
            lanternfishes_by_day[6] = 0
        if -1 in lanternfishes_by_day:
            lanternfishes_by_day[8] = lanternfishes_by_day[-1]
            lanternfishes_by_day[6] += lanternfishes_by_day[-1]
            lanternfishes_by_day.pop(-1)

    print(sum(l for l in lanternfishes_by_day.values()))
