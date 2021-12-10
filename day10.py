from pathlib import Path

syntax_costs = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

auto_complete_costs = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


closing_opening = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

opening_closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def read_input(input_path):
    lines = []
    with open(input_path, "r") as infile:
        for l in infile:
            line = list(l.strip())
            lines.append([value for value in line])
    return lines


def is_open(bracket):
    if bracket in ['(', '[', '{', '<']:
        return True
    return False


def second_task(input_path):
    lines = read_input(input_path)
    scores = []

    for line in lines:
        line_with_error = False
        stack = []
        auto_complete_score = 0
        for value in line:
            if is_open(value):
                stack.append(value)
            else:
                corresponding_bracket = stack.pop()
                if corresponding_bracket != closing_opening[value]:
                    line_with_error = True
                    break
        if not line_with_error:
            while stack:
                opening_bracket = stack.pop()
                closing_bracket = opening_closing[opening_bracket]
                auto_complete_score *= 5
                auto_complete_score += auto_complete_costs[closing_bracket]
            scores.append(auto_complete_score)
    scores.sort()
    print(scores[len(scores) // 2])


def first_task(input_path):
    lines = read_input(input_path)
    syntax_error_score = 0

    for line in lines:
        stack = []
        for value in line:
            if is_open(value):
                stack.append(value)
            else:
                corresponding_bracket = stack.pop()
                if corresponding_bracket != closing_opening[value]:
                    syntax_error_score += syntax_costs[value]
                    break

    print(syntax_error_score)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day10.txt')
    first_task(input_path)
    second_task(input_path)
