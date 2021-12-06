import numpy as np
from io import StringIO
from collections import defaultdict


def open_input():
    s = open("input.txt").read().replace(',', '\n')
    data = np.loadtxt(StringIO(s), dtype=int)
    return data


# Dumb way
""" def part_one(array):
    end = len(array)
    for j in range(0, 80):
        for i in range(0, end):
            if array[i] > 0:
                array[i] -= 1
            else:
                array[i] = 6
                array = np.append(array, [8])
                end += 1
    print("part one:", len(array)) """


def part_one():
    array = open_input()
    part_one = solution(array, 80)
    print("part one:", part_one)


def part_two():
    array = open_input()
    part_two = solution(array, 256)
    print("part two:", part_two)


def solution(array, n):
    dictionary = defaultdict(int)
    for i in array:
        dictionary[i] += 1
    for i in range(0, n):
        new_dictionary = defaultdict(int)
        for j in dictionary:
            num_lanternfish = dictionary[j]
            if j == 0:
                new_dictionary[6] += num_lanternfish
                new_dictionary[8] += num_lanternfish
            else:
                new_dictionary[j - 1] += num_lanternfish
        dictionary = new_dictionary
    ret = sum([dictionary[k] for k in dictionary])
    return ret


if __name__ == "__main__":
    part_one()
    part_two()
