from pathlib import Path
from collections import Counter


def read_input(input_path):
    # represent the graph by a dict of sets
    graph = dict()
    with open(input_path, "r") as infile:
        for l in infile:
            line = l.strip().split('-')
            if line[0] not in graph:
                graph[line[0]] = set()
            if line[1] not in graph:
                graph[line[1]] = set()
            graph[line[0]].add(line[1])
            graph[line[1]].add(line[0])

    return graph


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node.isupper() or (node.islower() and node not in path):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def allowed_node(path, current):
    frequencies = Counter(path)

    if current == 'start' and frequencies['start'] == 1:
        return False

    if current == 'end' and frequencies['end'] == 0:
        return True

    lower_path = [node for node in path if node.islower() and node != current]
    lower_path = list(set(lower_path))  # to prevent counting the same node twice and returning False
    lower_frequencies = [frequencies[node] for node in lower_path]
    freq_frequencies = Counter(lower_frequencies)

    # if another small node appeared twice and this is the first time for the current ==> allowed
    if freq_frequencies[2] == 1 and frequencies[current] == 0:
        return True
    # if no other small node appeared twice and the current didn't pass 2 appearances:
    elif freq_frequencies[2] == 0 and frequencies[current] < 2:
        return True

    return False


def find_all_paths_task_2(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node.isupper() or \
                (node.islower() and allowed_node(path, node)):
            newpaths = find_all_paths_task_2(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def first_task(input_path):
    graph = read_input(input_path)

    paths = find_all_paths(graph, 'start', 'end')

    for path in paths:
        print(path)

    print(f'number of paths = {len(paths)}')


def second_task(input_path):
    graph = read_input(input_path)

    paths = find_all_paths_task_2(graph, 'start', 'end')

    filtered_paths = []
    for path in paths:
        if path not in filtered_paths:
            filtered_paths.append(path)

    for path in filtered_paths:
        print(path)

    print(f'number of paths = {len(filtered_paths)}')


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day12.txt')
    first_task(input_path)
    second_task(input_path)
