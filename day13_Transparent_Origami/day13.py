import numpy as np
from contextlib import contextmanager


class Data:
    with open("input.txt") as fd:
        array = [i.split(",") for i in fd.read().splitlines()]
    i = 0
    while array[i] != ['']:
        i += 1
    points = [(int(x), int(y)) for x, y in array[:i]]
    i += 1
    array = array[i:]
    instructions = []
    for i in array:
        instructions.append(i[0].split("="))
    for i in range(len(instructions)):
        instructions[i][1] = int(instructions[i][1])


def fold_y(matrix, c, hor, ver):
    x = 0
    y = Data.instructions[c][1]
    for x in range(len(matrix[0])):
        matrix[y][x] = 0
    i = 0
    for y in range(len(matrix) - 1, Data.instructions[c][1], -1):
        j = 0
        for x in range(0, len(matrix[i])):
            matrix[i][j] = matrix[y][x] if matrix[y][x] == 1 else matrix[i][j]
            matrix[y][x] = 0
            j += 1
        i += 1
    return matrix


def fold_x(matrix, c, hor, ver):
    y = 0
    x = Data.instructions[c][1]
    for y in range(len(matrix)):
        matrix[y][x] = 0
    i = 0
    for y in range(0, len(matrix)):
        j = 0
        for x in range(len(matrix[0]) - 1, Data.instructions[c][1], -1):
            matrix[i][j] = matrix[y][x] if matrix[y][x] == 1 else matrix[i][j]
            matrix[y][x] = 0
            j += 1
        i += 1
    return matrix


def solution(Data, part):
    hor = 0
    ver = 0
    for i in range(0, len(Data.points)):
        hor = Data.points[i][0] if Data.points[i][0] > hor else hor
        ver = Data.points[i][1] if Data.points[i][1] > ver else ver
    hor += 1
    ver += 1
    matrix = np.zeros((ver, hor), int)
    for x, y in Data.points:
        matrix[y][x] = 1
    stop = 1 if part == "one" else len(Data.instructions)
    for c in range(0, stop):
        if (Data.instructions[c][0] == "fold along y"):
            matrix = fold_y(matrix, c, hor, ver)
            ver = int(ver / 2)
            matrix = matrix[:ver, :hor]
        elif (Data.instructions[c][0] == "fold along x"):
            matrix = fold_x(matrix, c, hor, ver)
            hor = int(hor / 2)
            matrix = matrix[:ver, :hor]
    return matrix


@contextmanager
def print_array_on_one_line():
    oldoptions = np.get_printoptions()
    np.set_printoptions(linewidth=np.inf)
    yield
    np.set_printoptions(**oldoptions)


def part_one(Data):
    matrix = solution(Data, "one")
    print("part one:", sum(sum(matrix)))


def part_two(Data):
    print("part two:")
    matrix = solution(Data, "two")
    with print_array_on_one_line():
        print(matrix)


if (__name__ == "__main__"):
    part_one(Data)
    part_two(Data)
