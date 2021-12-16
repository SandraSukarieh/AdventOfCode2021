from pathlib import Path
import sys
from queue import PriorityQueue
from copy import deepcopy


def read_input(input_path):
    lines = []
    with open(input_path, "r") as infile:
        for l in infile:
            line = list(l.strip())
            lines.append([int(value) for value in line])
    return lines


def read_input_part_2(matrix):
    original_matrix = deepcopy(matrix)
    rows = len(original_matrix)
    columns = len(original_matrix[0])
    assert id(original_matrix) != id(matrix)
    for tile in range(4):
        for row in range(rows):
            for column in range(columns):
                new_value = matrix[row][column + (tile*columns)] + 1
                if new_value == 10:
                    new_value = 1
                matrix[row].append(new_value)

    for tile in range(4):
        for row in range(rows):
            new_line = [x+1 for x in matrix[row + (tile*rows)]]
            for idx, n in enumerate(new_line):
                if n == 10:
                    new_line[idx] = 1
            matrix.append(new_line)


def build_graph(matrix):
    graph = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            graph[(i, j)] = []
            if i < len(matrix) - 1:
                graph[(i, j)].append((i+1, j))
            if j < len(matrix[0]) - 1:
                graph[(i, j)].append((i, j+1))
            if i-1 >= 0:
                graph[(i, j)].append((i-1, j))
            if j-1 >= 0:
                graph[(i, j)].append((i, j-1))
    return graph


def min_distance(matrix, neighbors, visited):
    min = sys.maxsize
    for neighbor in neighbors:
        if matrix[neighbor[0]][neighbor[1]] < min and not visited[(neighbor[0], neighbor[1])]:
            min = matrix[neighbor[0]][neighbor[1]]
            next_node = neighbor
    return next_node


def first_task(input_path):
    matrix = read_input(input_path)
    graph = build_graph(matrix)
    p = PriorityQueue()

    visited = dict()
    for node in graph:
        visited[node] = False

    current = (0, 0)
    end = (len(matrix) - 1, len(matrix[0]) -1)
    p.put((0, current))
    visited[current] = True

    while not p.empty():
        next_node = p.get()
        score = next_node[0]
        current = next_node[1]
        if current == end:
            break
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                next_score = matrix[node[0]][node[1]]
                p.put((score + next_score, node))
    print(score)


def second_task(input_path):

    matrix = read_input(input_path)
    read_input_part_2(matrix)
    graph = build_graph(matrix)
    p = PriorityQueue()

    visited = dict()
    for node in graph:
        visited[node] = False

    current = (0, 0)
    end = (len(matrix) - 1, len(matrix[0]) - 1)
    p.put((0, current))
    visited[current] = True

    while not p.empty():
        next_node = p.get()
        score = next_node[0]
        current = next_node[1]
        print(current)
        if current == end:
            break
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                next_score = matrix[node[0]][node[1]]
                p.put((score + next_score, node))
    print(score)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day15.txt')
    # first_task(input_path)
    second_task(input_path)
