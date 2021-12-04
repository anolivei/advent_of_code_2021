import numpy as np


def get_chosen_numbers():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    num = [int(s) for s in array[0].split(',')]
    return(num)


def get_rows():
    rows = np.loadtxt("input.txt", skiprows=1, dtype=int)
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


def part_one(num, rows, cols):
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


def part_two(num, rows, cols):
    print("part two:")


if (__name__ == "__main__"):
    num = get_chosen_numbers()
    rows = get_rows()
    cols = get_cols(rows)
    part_one(num, rows, cols)
    part_two(num, rows, cols)
