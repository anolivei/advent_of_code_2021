import statistics


def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    matrix = []
    for i in range(0, len(array)):
        matrix.append(list(array[i]))
    return matrix


def is_open(chunk):
    chunks = set(['(', '[', '{', '<'])
    chunk = set(chunk)
    if chunks >= chunk:
        return True
    return False


def is_pair(last, actual):
    if (
        (last == '(' and actual == ')') or
        (last == '[' and actual == ']') or
        (last == '{' and actual == '}') or
        (last == '<' and actual == '>')
    ):
        return True
    return False


def part_one(matrix):
    last = []
    ret = 0
    value = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for i in range(0, len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if is_open(matrix[i][j]):
                last.append(matrix[i][j])
                j += 1
            elif is_pair(last.pop(-1), matrix[i][j]):
                j += 1
            else:
                ret += value[matrix[i][j]]
                break
    print("part one:", ret)


def part_two(matrix):
    value = {'(': 1, '[': 2, '{': 3, '<': 4}
    a_ret = []
    for i in range(0, len(matrix)):
        last = []
        j = 0
        while j < len(matrix[i]):
            if is_open(matrix[i][j]):
                last.append(matrix[i][j])
                j += 1
            elif is_pair(last.pop(-1), matrix[i][j]):
                j += 1
            else:
                break
        if j == (len(matrix[i])):
            ret = 0
            k = len(last) - 1
            while k >= 0:
                ret = ret * 5 + value[last[k]]
                k -= 1
            a_ret.append(ret)
    print("part two:", statistics.median(a_ret))


if (__name__ == "__main__"):
    matrix = open_input()
    part_one(matrix)
    part_two(matrix)
