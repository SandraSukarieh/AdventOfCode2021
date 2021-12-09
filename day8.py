from pathlib import Path
import copy
from deepdiff import DeepDiff

ground_truth = {
    '0': ['a', 'b', 'c', 'e', 'f', 'g'],
    '1': ['c', 'f'],
    '2': ['a', 'c', 'd', 'e', 'g'],
    '3': ['a', 'c', 'd', 'f', 'g'],
    '4': ['b', 'c', 'd', 'f'],
    '5': ['a', 'b', 'd', 'f', 'g'],
    '6': ['a', 'b', 'd', 'e', 'f', 'g'],
    '7': ['a', 'c', 'f'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g']
}


def read_input(input_path):
    values = []
    with open(input_path, "r") as infile:
        for l in infile:
            l = l.split('|')
            input_values = l[0].strip().split()
            output_values = l[1].strip().split()
            values.append([input_values, output_values])
    return values


def first_task(input_path):
    values = read_input(input_path)
    unique_segments_counter = 0
    for value in values:
        output_values = value[1]
        for entry in output_values:
            if len(entry) in [2, 3, 4, 7]:
                unique_segments_counter += 1
    print(unique_segments_counter)


def link_entry_to_combinations(entry, ground_truth_entry, combinations_dict):
    true_combination = ground_truth[ground_truth_entry]
    for character in entry:
        if character not in combinations_dict:
            combinations_dict[character] = []
        combinations_dict[character].append(true_combination)


def check_entry_against_unique_segments(entry, combinations_dict):
    if len(entry) == 2:
        link_entry_to_combinations(entry, "1", combinations_dict)
    elif len(entry) == 4:
        link_entry_to_combinations(entry, "4", combinations_dict)
    elif len(entry) == 3:
        link_entry_to_combinations(entry, "7", combinations_dict)
    elif len(entry) == 7:
        link_entry_to_combinations(entry, "8", combinations_dict)


def get_intersections(entry_combinations):
    final_set = set(set(entry_combinations[0]).intersection(set(entry_combinations[1])))
    for i in range(2, len(entry_combinations)):
        temp = set(set(entry_combinations[i]).intersection(final_set))
        final_set = copy.deepcopy(temp)
    return final_set


# if 2 chars has 2 identical possibilities of length 3, then no other char should have any of those 2 possibilities
# this rule finds the letter a which is the difference between 1 and 7
def rule_1(combinations):
    while True:
        temp = copy.deepcopy(combinations)
        for v in combinations.values():
            v_keys = []
            keys_to_remove = []
            for k in combinations.keys():
                if v.intersection(combinations[k]):
                    if combinations[k] == v:
                        v_keys.append(k)
                    else:
                        keys_to_remove.append(k)
            if len(v_keys) == len(v):
                for k_to_remove in keys_to_remove:
                    for character in v:
                        combinations[k_to_remove].remove(character)
        diff = DeepDiff(temp, combinations, ignore_order=True)
        if len(diff) == 0:
            break


# find the number 3 as it's the only on of length 5 with c, f
# compare 3 with 9 (length 6 with one difference) to locate the encoding of b
# compare 9 with 8 to locate the encoding of e
def rule_2(combinations, input_values):
    three = None
    nine = None
    length_5_candidates = [v for v in input_values if len(v) == 5]  # 2, 3, 5
    c_f_solutions = [k for k in combinations.keys() if len(combinations[k].difference({'c', 'f'})) == 0]
    for candidate in length_5_candidates:
        if c_f_solutions[0] in candidate and c_f_solutions[1] in candidate:
            three = candidate
            break
    length_6_candidates = [v for v in input_values if len(v) == 6]  # 0, 6, 9
    for candidate in length_6_candidates:
        diff = set(candidate).difference(set(three))
        if len(diff) == 1:
            nine = candidate
            break
    b_encoding = diff.pop()
    combinations[b_encoding] = {'b'}
    for k, v in combinations.items():
        if 'b' in v and k != b_encoding:
            v.remove('b')

    eight = [v for v in input_values if len(v) == 7][0]
    diff = set(eight).difference(set(nine))
    e_encoding = diff.pop()
    combinations[e_encoding] = {'e'}
    for k, v in combinations.items():
        if 'e' in v and k != e_encoding:
            v.remove('e')


# compare with 2 to locate the encoding of c
def rule_3(combinations, input_values, encoding):
    length_5_candidates = [v for v in input_values if len(v) == 5]  # 2, 3, 5

    e_encoding = None
    for k, v in encoding.items():
        if v == 'e':
            e_encoding = k
            break

    two = [v for v in length_5_candidates if e_encoding in v][0]
    for character in two:
        if character not in encoding:
            encoding[character] = 'c'
            del combinations[character]
            for k in combinations:
                encoding[k] = 'f'
            break


def check_if_found(combinations, encoding):
    keys_to_remove = []
    for k, v in combinations.items():
        if len(v) == 1:
            encoding[k] = v.pop()
            keys_to_remove.append(k)
    for k_to_remove in keys_to_remove:
        del combinations[k_to_remove]


def encode_output(output_values, encoding):
    answer = []
    for value in output_values:
        true_values = set()
        for character in value:
            true_values.add(encoding[character])
        for number, original in ground_truth.items():
            if set(original) == true_values:
                answer.append(number)
                break
    return int("".join(answer))


def second_task(input_path):

    final_answer = 0

    inputs = read_input(input_path)
    for line in inputs:

        encoding = dict()
        combinations = dict()
        input_values = line[0]
        input_values = [list(v) for v in input_values]

        # get all possible initial encodings for each letter
        for v in input_values:
            check_entry_against_unique_segments(v, combinations)

        # get intersections ==> all valid encodings (possible solution) for each letter
        for k, v in combinations.items():
            if len(v) > 1:
                combinations[k] = get_intersections(v)
            else:
                combinations[k] = set(combinations[k][0])

        rule_1(combinations)
        check_if_found(combinations, encoding)

        rule_2(combinations, input_values)
        check_if_found(combinations, encoding)

        rule_3(combinations, input_values, encoding)

        output_values = line[1]
        output_values = [list(v) for v in output_values]
        final_answer += encode_output(output_values, encoding)

    print(final_answer)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day8.txt')
    first_task(input_path)
    second_task(input_path)
