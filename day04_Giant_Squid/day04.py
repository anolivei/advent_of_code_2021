import numpy as np


def get_chosen_numbers():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    num = [int(s) for s in array[0].split(',')]
    return(num)


def solution(num, part):
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    array = array[1:]
    a_matrix = []
    winners = []
    n_boards = 0
    i = 0
    while i < len(array):
        a_matrix.append(np.loadtxt(array[i:], dtype=int, max_rows=5))
        i += 6
        n_boards += 1
    for n in num:
        for i in range(0, n_boards):
            a_matrix[i] = np.where(a_matrix[i] == n, -1, a_matrix[i])
            row = np.where(a_matrix[i].sum(axis=0) == -5)
            col = np.where(a_matrix[i].sum(axis=1) == -5)
            if row[0].size > 0 or col[0].size > 0:
                if i not in winners:
                    winners.append(i)
            if check(part, winners, n_boards) == 1:
                break
        if check(part, winners, n_boards) == 1:
            break
    a_matrix[i] = np.where(a_matrix[i] == -1, 0, a_matrix[i])
    row = sum(a_matrix[i].sum(axis=0))
    return (row * n)


def check(part, winners, n_boards):
    if part == "one":
        if len(winners) == 1:
            return 1
    elif part == "two":
        if len(winners) == n_boards:
            return 1
    else:
        return 0


def part_one(num):
    ret = solution(num, "one")
    print("part one:", ret)


def part_two(num):
    ret = solution(num, "two")
    print("part two:", ret)


if (__name__ == "__main__"):
    num = get_chosen_numbers()
    part_one(num)
    part_two(num)
