from collections import defaultdict
from queue import PriorityQueue
import math


def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    matrix = []
    for i in range(0, len(array)):
        matrix.append(list(map(int, array[i])))
    return matrix


def check_borders(i, j, i_max, j_max):
    if i < 0 or i > i_max or j < 0 or j > j_max:
        return False
    return True


def neighborhood(i_max, j_max, i, j):
    neighbors = [
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1),
    ]
    n = []
    for neighbor in neighbors:
        if check_borders(neighbor[0], neighbor[1], i_max, j_max):
            n.append(neighbor)
    return n


def matrix_5x5(matrix, point):
    i_len = len(matrix)
    j_len = len(matrix[0])
    i = point[0] % i_len
    j = point[1] % j_len
    i_remainder = math.floor(point[0] / i_len)
    j_remainder = math.floor(point[1] / j_len)
    remainder = (i_remainder + j_remainder)
    ret = (matrix[i][j] + remainder) % 10
    value = math.floor((matrix[i][j] + remainder) / 10)
    ret += value
    return ret


def solution(part):
    matrix = open_input()
    multiplicator = 1 if part == "one" else 5
    i_max = multiplicator * len(matrix) - 1
    j_max = multiplicator * len(matrix[0]) - 1
    delta_s = defaultdict(lambda: 99999999)
    delta_s[(0, 0)] = 0
    past_points = set()
    future_points = PriorityQueue()
    future_points.put((0, (0, 0)))
    while not future_points.empty():
        (dist, point) = future_points.get()
        past_points.add(point)
        for neighbor in neighborhood(i_max, j_max, point[0], point[1]):
            if part == "one":
                next_dist = dist + matrix[neighbor[0]][neighbor[1]]
            elif part == "two":
                next_dist = dist + matrix_5x5(matrix, neighbor)
            if neighbor not in past_points and delta_s[neighbor] > next_dist:
                delta_s[neighbor] = next_dist
                future_points.put((next_dist, neighbor))
    return delta_s[i_max, j_max]


def part_one():
    ret = solution("one")
    print("part one:", ret)


def part_two():
    ret = solution("two")
    print("part two:", ret)


if (__name__ == "__main__"):
    part_one()
    part_two()
