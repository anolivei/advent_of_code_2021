import numpy as np


def part_one(num):
    rows = get_rows()
    cols = get_cols(rows)
    for n in range(0, len(num)):
        for i in range(0, len(rows)):
            if sum(rows[i]) == -5 or sum(cols[i]) == -5:
                break
            for j in range(0, 5):
                if sum(rows[i]) == -5 or sum(cols[i]) == -5:
                    break
                if rows[i][j] == num[n]:
                    rows[i][j] = -1
                if cols[i][j] == num[n]:
                    cols[i][j] = -1
        if sum(rows[i]) == -5 or sum(cols[i]) == -5:
            break
    first_line = i - (i % 5)
    last_line = first_line + 5
    result = 0
    for i in range(first_line, last_line):
        for j in range(0, 5):
            if rows[i][j] > 0:
                result += rows[i][j]
    print("part one:", num[n - 1] * result)


def get_chosen_numbers():
    with open("input_test.txt") as fd:
        array = fd.read().splitlines()
    num = [int(s) for s in array[0].split(',')]
    return(num)


def get_rows():
    rows = np.loadtxt("input_test.txt", skiprows=1, dtype=int)
    return rows


def get_cols(rows):
    col = []
    m = 0
    while m < len(rows):
        for j in range(0, 5):
            for i in range(m, m + 5):
                col.append(rows[i][j])
        m += 5
    col = np.array(split(col, 5))
    return col


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def part_two(num):
    with open("input_test.txt") as fd:
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
                if len(winners) == n_boards:
                    break
        if len(winners) == n_boards:
            break
    a_matrix[i] = np.where(a_matrix[i] == -1, 0, a_matrix[i])
    row = sum(a_matrix[i].sum(axis=0))
    print("part two:", row * n)


if (__name__ == "__main__"):
    num = get_chosen_numbers()
    part_one(num)
    part_two(num)
