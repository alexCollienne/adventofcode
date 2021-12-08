def _get_pattern_from_matches(
    segments: set,
    segment_out_pattern_only: str,
    available_patterns: list,
) -> str:
    return next(
        (
            ap
            for ap in available_patterns
            if segments.intersection(segment_out_pattern_only).issubset(ap)
        ),
    )


def _get_pattern_from_differences(
    segments: set,
    segment_in_pattern_only: str,
    available_patterns: list,
) -> str:
    return next(
        (
            ap
            for ap in available_patterns
            if segments.difference(segment_in_pattern_only).issubset(ap)
        ),
    )


def _get_patterns(digits_patterns: list[str]) -> tuple:
    segments = set("abcdefg")

    one = next(dp for dp in digits_patterns if len(dp) == 2)
    four = next(dp for dp in digits_patterns if len(dp) == 4)
    seven = next(dp for dp in digits_patterns if len(dp) == 3)
    height = next(dp for dp in digits_patterns if len(dp) == 7)

    two_or_three_or_five = [dp for dp in digits_patterns if len(dp) == 5]
    two = _get_pattern_from_differences(segments, seven + four, two_or_three_or_five)
    two_or_three_or_five.remove(two)
    three = _get_pattern_from_matches(segments, one, two_or_three_or_five)
    two_or_three_or_five.remove(three)
    five = two_or_three_or_five[0]

    zero_or_nine_or_six = [dp for dp in digits_patterns if len(dp) == 6]
    six = next((dp for dp in zero_or_nine_or_six if len(set(one).difference(dp)) == 1))
    zero_or_nine_or_six.remove(six)
    zero = next(
        (dp for dp in zero_or_nine_or_six if len(set(four).difference(dp)) == 1)
    )
    zero_or_nine_or_six.remove(zero)
    nine = zero_or_nine_or_six[0]

    return zero, one, two, three, four, five, six, seven, height, nine


def _get_digits(line: str) -> int:
    patterns = _get_patterns(line.split(" | ")[0].split(" "))
    return int(
        "".join(
            [
                _get_digit(patterns, digit_pattern)
                for digit_pattern in line.split(" | ")[1].split(" ")
            ]
        )
    )


def _get_digit(patterns: tuple, digit_pattern: str) -> str:
    for digit, pattern in enumerate(patterns):
        if set(pattern) == set(digit_pattern):
            return str(digit)


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    digits = [_get_digits(line.rstrip()) for line in my_file.readlines()]
    print(sum(digits))
