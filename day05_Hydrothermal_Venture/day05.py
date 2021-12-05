import numpy as np
from io import StringIO


def open_input():
    s = open("input.txt").read().replace('->', '').replace(',', ' ')
    data = np.loadtxt(StringIO(s), dtype=int)
    return data


def create_matrix():
    matrix = np.zeros((1000, 1000), dtype=np.int32)
    return matrix


def part_one(array, matrix):
    count = 0
    for i in range(0, len(array)):
        x1 = array[i][0]
        y1 = array[i][1]
        x2 = array[i][2]
        y2 = array[i][3]
        if (x1 == x2 or y1 == y2):
            j = 0
            if x1 != x2:
                j = x1 if x1 < x2 else x2
                k = x1 if x1 > x2 else x2
                while j <= k:
                    matrix[y1][j] += 1
                    if(matrix[y1][j] == 2):
                        count += 1
                    j += 1
            elif y1 != y2:
                j = y1 if y1 < y2 else y2
                k = y1 if y1 > y2 else y2
                while j <= k:
                    matrix[j][x1] += 1
                    if(matrix[j][x1] == 2):
                        count += 1
                    j += 1
    print("part one:", count)


def part_two():
    print("part two:")


if __name__ == "__main__":
    array = open_input()
    matrix = create_matrix()
    part_one(array, matrix)
    part_two()
