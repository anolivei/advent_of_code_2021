def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    matrix = []
    for i in range(0, len(array)):
        matrix.append(list(map(int, array[i])))
    return matrix


def part_one(matrix):
    lowers = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            num = matrix[i][j]
            try:
                right = matrix[i][j + 1]
            except IndexError:
                right = 1000
            if j > 0:
                left = matrix[i][j - 1]
            else:
                left = 1000
            try:
                up = matrix[i + 1][j]
            except IndexError:
                up = 1000
            if i > 0:
                down = matrix[i - 1][j]
            else:
                down = 1000
            if num < right and num < left and num < up and num < down:
                lowers.append(matrix[i][j])
    ret = sum(lowers) + len(lowers)
    print("part one:", ret)


def part_two(matrix):
    print("part two:")


if (__name__ == "__main__"):
    matrix = open_input()
    part_one(matrix)
    part_two(matrix)
