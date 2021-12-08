import statistics
import math


def open_input():
    with open("input.txt") as fd:
        array = fd.read()
    array = [x.strip() for x in array.split(',')]
    array = list(map(int, array))
    return array


def part_one(array):
    posiction = int(statistics.median(array))
    ret = 0
    for i in range(0, len(array)):
        ret += abs(array[i] - posiction)
    print("part one:", ret)


def part_two(array):
    posiction = math.floor(statistics.mean(array))
    ret = 0
    for i in range(0, len(array)):
        ret += sum_factorial(abs(array[i] - posiction))
    print("part two:", ret)


def sum_factorial(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i
    return ret


if (__name__ == "__main__"):
    array = open_input()
    part_one(array)
    part_two(array)
