def _format_program(lines) -> list[dict]:
    return [
        {
            "cmd": line.split(" ")[0],
            "param": int(line.split(" ")[1]),
            "used": False,
        }
        for line in lines
    ]


def _run_line(instruction: dict[str, int, bool], accumulator: int) -> tuple:
    key_editor = 1
    if instruction["cmd"] == "acc":
        accumulator += instruction["param"]
    elif instruction["cmd"] == "jmp":
        key_editor = instruction["param"]

    instruction["used"] = True
    return key_editor, accumulator


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    instructions = _format_program(my_file.readlines())
    key = 0
    accumulator = 0
    while not instructions[key]["used"]:
        key_editor, accumulator = _run_line(instructions[key], accumulator)
        key += key_editor

    print(accumulator)
