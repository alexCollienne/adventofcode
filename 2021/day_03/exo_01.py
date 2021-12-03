from functools import reduce


def _reducer(groups: list[list], binary: str) -> list[list]:
    for i, number in enumerate(binary):
        if len(groups) < i + 1:
            groups.append([number])
        else:
            groups[i].append(number)

    return groups


my_file = open("input.txt", "r")
binaries = [l.rstrip() for l in my_file.readlines()]
reduced = reduce(_reducer, binaries, [])
gamma = "".join([max(set(r), key=r.count) for r in reduced])
epsilon = "".join([str(abs(int(n) - 1)) for n in gamma])
print(int(gamma, 2) * int(epsilon, 2))
