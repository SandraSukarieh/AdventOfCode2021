from pathlib import Path


def read_input(input_path):
    values = []
    with open(input_path, "r") as infile:
        for l in infile:
            line_values = l.strip().replace(',', ' ').split()
            line_values = [int(value) for value in line_values]
            values = values + line_values
    return values


def shifting(fish_list):
    temp = fish_list[0]
    for i in range(8):
        fish_list[i] = fish_list[i+1]
    fish_list[8] = temp
    fish_list[6] += temp


def first_task(input_path, days):
    values = read_input(input_path)
    fish_list = [0]*9
    for value in values:
        fish_list[value] += 1

    for i in range(days):
        shifting(fish_list)
    print(sum(fish_list))


def second_task(input_path, days):
    values = read_input(input_path)
    fish_list = [0]*9
    for value in values:
        fish_list[value] += 1

    for i in range(days):
        shifting(fish_list)
    print(sum(fish_list))


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day6.txt')
    first_task(input_path, 80)
    second_task(input_path, 256)
