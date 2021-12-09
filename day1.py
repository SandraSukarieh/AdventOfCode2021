from pathlib import Path


def first_task(input_path):
    with open(input_path, 'r') as input:
        input_values = [int(depth.strip()) for depth in input]
        # input_values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        increased = 0
        for i in range(1, len(input_values)):
            if input_values[i] > input_values[i-1]:
                increased += 1
        print(increased)


def get_window_sum(values, start_index):
    return values[start_index] + values[start_index+1] + values[start_index+2]


def second_task(input_path):
    with open(input_path, 'r') as input:
        input_values = [int(depth.strip()) for depth in input]
        # input_values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        increased = 0
        for i in range(len(input_values)-3):
            first_window_sum = get_window_sum(input_values, i)
            second_window_sum = get_window_sum(input_values, i+1)
            if second_window_sum > first_window_sum:
                increased += 1
        print(increased)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day1.txt')
    first_task(input_path)
    second_task(input_path)
