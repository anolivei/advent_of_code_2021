from collections import defaultdict
from queue import PriorityQueue


def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    matrix = []
    for i in range(0, len(array)):
        matrix.append(list(map(int, array[i])))
    return matrix


def neighborhood(i_max, j_max, i, j):
    neighbors = [
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
    ]
    n = []
    for neighbor in neighbors:
        if i < 0 or i > i_max or j < 0 or j > j_max:
            continue
        n.append(neighbor)
    return n


def value(matrix, point):
    i_len = len(matrix)
    j_len = len(matrix[0])
    i = point[0] % i_len
    j = point[1] % j_len
    ret = matrix[i][j] + point[0]//i_len + point[1]//j_len
    while ret > 9:
        ret -= 9
    return ret


def solution(n_tiles):
    matrix = open_input()
    i_max = n_tiles * len(matrix) - 1
    j_max = n_tiles * len(matrix[0]) - 1
    delta_s = defaultdict(lambda: 99999999)
    delta_s[(0, 0)] = 0
    visited = set()
    unvisited = PriorityQueue()
    unvisited.put((0, (0, 0)))
    while not unvisited.empty():
        (dist, point) = unvisited.get()
        visited.add(point)
        for neighbor in neighborhood(i_max, j_max, point[0], point[1]):
            next_dist = dist + value(matrix, neighbor)
            if neighbor not in visited and delta_s[neighbor] > next_dist:
                delta_s[neighbor] = next_dist
                unvisited.put((next_dist, neighbor))
    return delta_s[i_max, j_max]


def part_one():
    ret = solution(1)
    print("part one:", ret)


def part_two():
    ret = solution(5)
    print("part two:", ret)


if (__name__ == "__main__"):
    part_one()
    part_two()
