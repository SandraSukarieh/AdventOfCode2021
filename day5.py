from pathlib import Path


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"


class Line:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2

    def is_vertical(self):
        if self.start.y == self.end.y:
            return True
        return False

    def is_horizontal(self):
        if self.start.x == self.end.x:
            return True
        return False

    def get_vertical_points(self):
        points = []
        if self.end.x > self.start.x:
            first_point = Point(self.start.x, self.start.y)
            last_point = Point(self.end.x, self.end.y)
        else:
            first_point = Point(self.end.x, self.end.y)
            last_point = Point(self.start.x, self.start.y)

        initial_x = first_point.x + 1
        points.append(first_point)
        while initial_x < last_point.x:
            points.append(Point(initial_x, first_point.y))
            initial_x += 1
        points.append(last_point)

        return points

    def get_horizontal_points(self):
        points = []
        if self.end.y > self.start.y:
            first_point = Point(self.start.x, self.start.y)
            last_point = Point(self.end.x, self.end.y)
        else:
            first_point = Point(self.end.x, self.end.y)
            last_point = Point(self.start.x, self.start.y)

        initial_y = first_point.y + 1
        points.append(first_point)
        while initial_y < last_point.y:
            points.append(Point(first_point.x, initial_y))
            initial_y += 1
        points.append(last_point)

        return points

    def get_diagonal_points(self):
        points = []
        xs = []
        ys = []
        if self.start.x < self.end.x:
            first_point = Point(self.start.x, self.start.y)
            last_point = Point(self.end.x, self.end.y)
        else:
            first_point = Point(self.end.x, self.end.y)
            last_point = Point(self.start.x, self.start.y)

        for i in range(first_point.x, last_point.x+1):
            xs.append(i)
        if first_point.y < last_point.y:
            for j in range(first_point.y, last_point.y + 1):
                ys.append(j)
        else:
            for j in range(first_point.y, last_point.y - 1, -1):
                ys.append(j)

        assert len(xs) == len(ys)
        for k in range(len(xs)):
            points.append(Point(xs[k], ys[k]))

        return points


def read_input(input_path):
    lines = []
    unique_values = set()
    with open(input_path, "r") as infile:
        for l in infile:
            values = l.strip().replace('->', ' ').replace(',', ' ').split()
            values = [int(value) for value in values]
            if len(values) == 4:
                unique_values.update(set(values))
                start = Point(values[0], values[1])
                end = Point(values[2], values[3])
                lines.append(Line(start, end))
    return unique_values, lines


def first_task(input_path):
    unique_values, lines = read_input(input_path)
    grid_size = max(unique_values) + 1
    grid = [[0]*grid_size for i in range(grid_size)]
    for line in lines:
        points = []
        if line.is_vertical():
            points = line.get_vertical_points()
        elif line.is_horizontal():
            points = line.get_horizontal_points()
        for point in points:
            # swapped to be printed as the example!
            grid[point.y][point.x] += 1
    counter = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] > 1:
                counter += 1
    print(counter)


def second_task(input_path):
    unique_values, lines = read_input(input_path)
    grid_size = max(unique_values) + 1
    grid = [[0] * grid_size for i in range(grid_size)]
    for line in lines:
        if line.is_vertical():
            points = line.get_vertical_points()
        elif line.is_horizontal():
            points = line.get_horizontal_points()
        else:
            points = line.get_diagonal_points()
        for point in points:
            grid[point.y][point.x] += 1
    counter = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] > 1:
                counter += 1
    print(counter)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day5.txt')
    first_task(input_path)
    second_task(input_path)
