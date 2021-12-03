from copy import copy, deepcopy


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


def _edit_instructions(instructions: list[dict], attempt: int) -> dict:
    count = 0
    for instruction in instructions:
        if instruction["cmd"] in ["jmp", "nop"]:
            if count == attempt and not (
                instruction["cmd"] == "nop" and instruction["param"] == "+0"
            ):
                instruction["cmd"] = "jmp" if instruction["cmd"] == "nop" else "nop"
                break
            else:
                count += 1

    return instructions


if __name__ == "__main__":
    my_file = open("input.txt", "r")
    instructions = _format_program(my_file.readlines())
    key = 0
    attempt = 0
    while attempt <= len(instructions) - 1 and key < len(instructions) - 1:
        print(f"----------------------------- Attempt {attempt}")
        edited_instructions = _edit_instructions(deepcopy(instructions), attempt)
        attempt += 1
        accumulator = 0
        key = 0
        while not edited_instructions[key]["used"] and key < len(instructions) - 1:
            line = edited_instructions[key]
            # print(f"Rune line : {key} - Accumulator : {accumulator}")
            key_editor, accumulator = _run_line(edited_instructions[key], accumulator)
            key += key_editor

    print(f"Accumalator {accumulator} at line {key}")
