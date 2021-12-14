from pathlib import Path


def read_input(input_path):
    coordinate_points = []
    folds = []
    coordinates = True
    with open(input_path, "r") as infile:
        for l in infile:
            if l == '\n':
                coordinates = False
                continue
            if coordinates:
                line = l.strip().split(',')
                line = [int(v) for v in line]
                coordinate_points.append([line[0], line[1]])
            else:
                fold = l.strip().split()[-1].split('=')
                fold[1] = int(fold[1])
                folds.append(fold)

    return coordinate_points, folds


def print_grid(grid):
    for row in grid:
        print(row)


def perform_horizontal_fold(fold_line, coordinate_points):
    for point in coordinate_points:
        if point[1] > fold_line:
            distance = point[1] - fold_line
            point[1] = fold_line - distance


def perform_vertical_fold(fold_line, coordinate_points):
    for point in coordinate_points:
        if point[0] > fold_line:
            distance = point[0] - fold_line
            point[0] = fold_line - distance


def filter_points(points):
    filtered_points = []
    for point in points:
        if point not in filtered_points:
            filtered_points.append(point)
    return filtered_points


def first_task(input_path):
    coordinate_points, folds = read_input(input_path)
    for fold in folds:
        if fold[0] == 'y':
            perform_horizontal_fold(fold[1], coordinate_points)
            coordinate_points = filter_points(coordinate_points)
            print(len(coordinate_points))
        else:
            perform_vertical_fold(fold[1], coordinate_points)
            coordinate_points = filter_points(coordinate_points)
            print(len(coordinate_points))
        break


def get_max_coordinate(coordinate_points):
    max_coordinate = 0
    for point in coordinate_points:
        if max(point) > max_coordinate:
            max_coordinate = max(point)
    return max_coordinate


def second_task(input_path):
    coordinate_points, folds = read_input(input_path)
    for fold in folds:
        if fold[0] == 'y':
            perform_horizontal_fold(fold[1], coordinate_points)
            coordinate_points = filter_points(coordinate_points)
        else:
            perform_vertical_fold(fold[1], coordinate_points)
            coordinate_points = filter_points(coordinate_points)

    max_coordinate = get_max_coordinate(coordinate_points)
    grid = [['.']*(max_coordinate+1) for i in range(max_coordinate+1)]
    for point in coordinate_points:
        grid[point[1]][point[0]] = '#'
    print_grid(grid)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day13.txt')
    first_task(input_path)
    second_task(input_path)
