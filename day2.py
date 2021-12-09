from pathlib import Path


def first_task(input_path):
    with open(input_path, 'r') as input:
        input_values = [input_value.strip() for input_value in input]
        horizontal_position = 0
        depth = 0
        for value in input_values:
            split_value = value.split()
            if split_value[0] == "forward":
                horizontal_position += int(split_value[1])
            elif split_value[0] == "down":
                depth += int(split_value[1])
            elif split_value[0] == "up":
                depth -= int(split_value[1])
        print(horizontal_position * depth)


def second_task(input_path):
    with open(input_path, 'r') as input:
        input_values = [input_value.strip() for input_value in input]
        horizontal_position = 0
        depth = 0
        aim = 0
        for value in input_values:
            split_value = value.split()
            if split_value[0] == "forward":
                horizontal_position += int(split_value[1])
                depth += aim * int(split_value[1])
            elif split_value[0] == "down":
                aim += int(split_value[1])
            elif split_value[0] == "up":
                aim -= int(split_value[1])
        print(horizontal_position * depth)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day2.txt')
    first_task(input_path)
    second_task(input_path)
