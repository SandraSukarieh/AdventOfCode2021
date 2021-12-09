from pathlib import Path


class Cell:
    def __init__(self, value):
        self.value = value
        self.visited = False


def read_input(input_path):
    lines = []
    with open(input_path, "r") as infile:
        for l in infile:
            line = list(l.strip())
            lines.append([int(value) for value in line])
    return lines


def read_input_with_instances(input_path):
    lines = []
    with open(input_path, "r") as infile:
        for l in infile:
            line = list(l.strip())
            cells = []
            for value in line:
                cell = Cell(int(value))
                cells.append(cell)
            lines.append(cells)
    return lines


def first_task(input_path):
    lines = read_input(input_path)
    risk_level = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 9:
                continue
            if j != 0 and lines[i][j] >= lines[i][j-1]:
                continue
            if j != len(lines[0]) -1 and lines[i][j] >= lines[i][j+1]:
                continue
            if i != 0 and lines[i][j] >= lines[i-1][j]:
                continue
            if i != len(lines)-1 and lines[i][j] >= lines[i+1][j]:
                continue
            else:
                risk_level += lines[i][j] + 1
    print(risk_level)


def check_validity(lines, i, j):
    if i < 0 or i > len(lines) - 1 or j < 0 or j > len(lines[0]) - 1 or lines[i][j].value == 9 or lines[i][j].visited:
        return False
    return True


def traverse(lines, i, j, counter):
    lines[i][j].visited = True
    if lines[i][j].value != 9:
        counter += 1
    if not (check_validity(lines, i-1, j)
            or check_validity(lines, i+1, j)
            or check_validity(lines, i, j-1)
            or check_validity(lines, i, j+1)):
        return counter
    if check_validity(lines, i-1, j):
        counter = traverse(lines, i-1, j, counter)
    if check_validity(lines, i+1, j):
        counter = traverse(lines, i+1, j, counter)
    if check_validity(lines, i, j-1):
        counter = traverse(lines, i, j-1, counter)
    if check_validity(lines, i, j+1):
        counter = traverse(lines, i, j+1, counter)
    return counter


def second_task(input_path):
    lines = read_input_with_instances(input_path)
    basins = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            size = traverse(lines, i, j, 0)
            if size > 1:
                basins.append(size)
    if basins:
        basins.sort(reverse=True)
        print(basins[0] * basins[1] * basins[2])


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day9.txt')
    first_task(input_path)
    second_task(input_path)
