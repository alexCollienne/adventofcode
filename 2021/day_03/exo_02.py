import collections


def _compute_binary(binaries: list[str], oxygen_generator_rating=True) -> int:
    i = 0
    while i < len(binaries[0]) and len(binaries) > 1:
        count_n = collections.Counter([n[i] for n in binaries])
        if oxygen_generator_rating:
            keep_n = (
                "1"
                if count_n["1"] == count_n["0"] or count_n["1"] > count_n["0"]
                else "0"
            )
        else:
            keep_n = (
                "0"
                if count_n["1"] == count_n["0"] or count_n["0"] < count_n["1"]
                else "1"
            )

        s = slice(i, i + 1)
        binaries = [b for b in binaries if b[s] == keep_n]
        i += 1

    return int(binaries[0], 2)


my_file = open("input.txt", "r")
binaries = [line.rstrip() for line in my_file.readlines()]

o2_rating = _compute_binary(binaries)
co2_rating = _compute_binary(binaries, False)

print(co2_rating * o2_rating)
