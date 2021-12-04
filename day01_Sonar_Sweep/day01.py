def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
    array = list(map(int, array))
    return array


def part_one(array):
    lenght = len(array)
    increased = 0
    for i in range(0, lenght - 1):
        if array[i] < array[i + 1]:
            increased += 1
    print("part one:", increased)


def part_two(array):
    lenght = len(array)
    increased = 0
    for i in range(0, lenght - 3):
        sum1 = array[i] + array[i + 1] + array[i + 2]
        sum2 = array[i + 1] + array[i + 2] + array[i + 3]
        if sum1 < sum2:
            increased += 1
    print("part two:", increased)


if (__name__ == "__main__"):
    array = open_input()
    part_one(array)
    part_two(array)
