from pathlib import Path
from statistics import mean


def read_input(input_path):
    values = []
    with open(input_path, "r") as infile:
        for l in infile:
            line_values = l.strip().replace(',', ' ').split()
            line_values = [int(value) for value in line_values]
            values = values + line_values
    return values


def calculate_sum_of_integers(n):
    sum = 0
    for num in range(1, n + 1, 1):
        sum = sum + num
    return sum


def first_task(input_path):
    values = read_input(input_path)
    values.sort()
    median_index = len(values) // 2
    list_median = values[median_index - 1]
    sum = 0
    for i in range(len(values)):
        sum += abs(values[i] - list_median)
    print(sum)


def second_task(input_path):
    values = read_input(input_path)
    values.sort()
    list_mean = mean(values)
    first_value = int(list_mean)
    second_value = first_value + 1
    fist_fuel_sum = 0
    for i in range(len(values)):
        fist_fuel_sum += calculate_sum_of_integers(abs(values[i] - first_value))
    second_fuel_sum = 0
    for i in range(len(values)):
        second_fuel_sum += calculate_sum_of_integers(abs(values[i] - second_value))
    min_fuel = second_fuel_sum if fist_fuel_sum > second_fuel_sum else fist_fuel_sum
    print(min_fuel)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day7.txt')
    first_task(input_path)
    second_task(input_path)
