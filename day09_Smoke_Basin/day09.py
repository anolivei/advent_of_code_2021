def open_input():
    with open("input_test.txt") as fd:
        array = fd.read().splitlines()
    matrix = []
    for i in range(0, len(array)):
        matrix.append(list(map(int, array[i])))
    return matrix


def part_one(matrix):
    lowers = []
    lowers_coord = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            num = matrix[i][j]
            try:
                right = matrix[i][j + 1]
            except IndexError:
                right = 1000
            left = matrix[i][j - 1] if j > 0 else 1000
            try:
                up = matrix[i + 1][j]
            except IndexError:
                up = 1000
            down = matrix[i - 1][j] if i > 0 else 100
            if num < right and num < left and num < up and num < down:
                lowers.append(matrix[i][j])
                lowers_coord.add((i, j))
    ret = sum(lowers) + len(lowers)
    print("part one:", ret)
    return (lowers_coord)


def part_two(matrix, lowers):
    a_size = []
    for lower in lowers:
        basin_size = 0
        a_around = [lower]
        basin = set()
        while len(a_around) > 0:
            around = a_around.pop(0)
            i = around[0]
            j = around[1]
            if around not in basin:
                if not(
                    i < 0 or i > (len(matrix) - 1) or
                    j < 0 or j > (len(matrix[0]) - 1) or
                    matrix[i][j] == 9 or matrix[i][j] == -1
                ):
                    basin_size += 1
                    basin.add(around)
                    a_around.append((i, j + 1))
                    a_around.append((i, j - 1))
                    a_around.append((i + 1, j))
                    a_around.append((i - 1, j))
        a_size.append(basin_size)
    a_size.sort(reverse=True)
    ret = a_size[0] * a_size[1] * a_size[2]
    print("part two:", ret)


if (__name__ == "__main__"):
    matrix = open_input()
    lowers = part_one(matrix)
    part_two(matrix, lowers)
