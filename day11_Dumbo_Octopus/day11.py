from collections import defaultdict


def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    matrix = []
    for i in range(0, len(array)):
        matrix.append(list(map(int, array[i])))
    return matrix


def surroundings(i_init, j_init, i_max, j_max):
    around = []
    for i in range(i_init - 1, i_init + 2):
        for j in range(j_init - 1, j_init + 2):
            if (
                (j != j_init or i != i_init) and not
                (i < 0 or i > i_max or j < 0 or j > j_max)
            ):
                around.append((i, j))
    return around


def solution(step_max, part):
    init = 0 if part == "one" else 1
    matrix = open_input()
    flash = 0
    hor = len(matrix[0])
    ver = len(matrix)
    coord = []
    for step in range(init, step_max):
        flashed = defaultdict(int)
        for i in range(0, ver):
            for j in range(0, hor):
                if matrix[i][j] > 9:
                    matrix[i][j] = 0
                coord.append((i, j))
        while len(coord) > 0:
            i, j = coord.pop()
            matrix[i][j] += 1
            if matrix[i][j] > 9 and not flashed[(i, j)]:
                flash += 1
                flashed[(i, j)] = 1
                for around in surroundings(i, j, ver - 1, hor - 1):
                    coord.append(around)
        if part == "two" and len(flashed) == ver * hor:
            return step
    if part == "one":
        return flash


def part_one():
    ret = solution(100, "one")
    print("part one:", ret)


def part_two():
    ret = solution(999, "two")
    print("part two:", ret)


if (__name__ == "__main__"):
    part_one()
    part_two()
