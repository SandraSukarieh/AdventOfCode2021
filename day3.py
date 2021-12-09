from pathlib import Path
from collections import Counter
import copy


def first_task(input_path):
    with open(input_path, 'r') as input:
        input_values = [input_value.strip() for input_value in input]
        gamma = ""
        epsilon = ""
        for i in range(len(input_values[0])):
            column = "".join([row[i] for row in input_values])
            counted_values = Counter(column)
            most_common_bit = "0" if counted_values["0"] > counted_values["1"] else "1"
            least_common_bit = "0" if most_common_bit == "1" else "1"
            gamma += most_common_bit
            epsilon += least_common_bit
        print(int(gamma, 2) * int(epsilon, 2))


def filter(input_values, position, is_most_common):
    column = "".join([row[position] for row in input_values])
    counted_values = Counter(column)
    most_common_bit = "0" if counted_values["0"] > counted_values["1"] else "1"
    least_common_bit = "0" if most_common_bit == "1" else "1"
    required_bit = most_common_bit if is_most_common else least_common_bit
    return [value for value in input_values if value[position] == required_bit]


def second_task(input_path):
    with open(input_path, 'r') as input:
        input_values = [input_value.strip() for input_value in input]
        oxygen_list = copy.deepcopy(input_values)
        carbon_list = copy.deepcopy(input_values)

        position = 0
        while len(oxygen_list) > 1:
            oxygen_list = filter(oxygen_list, position, True)
            position += 1
        oxygen_generator_rating = int(oxygen_list[0], 2)

        position = 0
        while len(carbon_list) > 1:
            carbon_list = filter(carbon_list, position, False)
            position += 1
        CO2_scrubber_rating = int(carbon_list[0], 2)

        print(oxygen_generator_rating * CO2_scrubber_rating)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day3.txt')
    first_task(input_path)
    second_task(input_path)
