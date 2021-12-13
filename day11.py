from pathlib import Path


class Cell:
    def __init__(self, value):
        self.value = value
        self.flashed = False


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


def read_input(input_path):
    lines = []
    with open(input_path, "r") as infile:
        for l in infile:
            line = list(l.strip())
            lines.append([int(value) for value in line])
    return lines


def increase_adjacents_by_one(grid, i, j):
    adjacents = [(i - 1, j),
                 (i + 1, j),
                 (i, j - 1),
                 (i, j + 1),
                 (i - 1, j - 1),
                 (i - 1, j + 1),
                 (i + 1, j - 1),
                 (i + 1, j + 1)]
    adjacents = [adjacent for adjacent in adjacents if 10 > adjacent[0] > -1 and 10 > adjacent[1] > -1]
    for adjacent in adjacents:
        grid[adjacent[0]][adjacent[1]].value += 1


def reset_flashed(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j].flashed = False


def increase_grid_by_one(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j].value += 1


def set_flashed_to_zero(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].flashed:
                grid[i][j].value = 0


def are_all_flashed(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j].flashed:
                return False
    return True


def catch_nine(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].value > 9 and not grid[i][j].flashed:
                grid[i][j].flashed = True
                return i, j
    return None, None


def flashes_per_step(grid):
    flashes = 0
    while True:
        i, j = catch_nine(grid)
        if i is not None:
            flashes += 1
            increase_adjacents_by_one(grid, i, j)
        else:
            break
    return flashes


def first_task(input_path):
    flashes = 0
    grid = read_input_with_instances(input_path)
    n_steps = 100
    for step in range(n_steps):
        reset_flashed(grid)
        increase_grid_by_one(grid)
        flashes += flashes_per_step(grid)
        set_flashed_to_zero(grid)
        print(f'after step {step+1}')
        for row in grid:
            print([cell.value for cell in row])
        print('\n')
    print(flashes)


def second_task(input_path):
    flashes = 0
    grid = read_input_with_instances(input_path)
    n_steps = 200
    step = 1
    while True:
        reset_flashed(grid)
        increase_grid_by_one(grid)
        flashes += flashes_per_step(grid)
        set_flashed_to_zero(grid)
        if are_all_flashed(grid):
            print(f'step during which all octopuses flash is {step}')
            break
        step += 1


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day11.txt')
    first_task(input_path)
    second_task(input_path)
