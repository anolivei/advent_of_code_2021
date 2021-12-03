def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
        fd.close()
    return array


def part_one(array):
    length_array = len(array)
    length_binary = len(array[0])
    gamma = ""
    epsilon = ""
    for j in range(0, length_binary):
        one = 0
        zero = 0
        for i in range(0, length_array):
            if array[i][j] == '1':
                one += 1
            elif array[i][j] == '0':
                zero += 1
        if one > zero:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
    print("part one:", int(gamma, 2) * int(epsilon, 2))


def filter_binary(array, length_binary, oc):
    for j in range(0, length_binary):
        array_one = []
        array_zero = []
        length_array = len(array)
        one = 0
        zero = 0
        if (length_array > 1):
            for i in range(0, length_array):
                if array[i][j] == '1':
                    one += 1
                    array_one.append(array[i])
                elif array[i][j] == '0':
                    zero += 1
                    array_zero.append(array[i])
            if (oc == 'o'):
                if one >= zero:
                    array = array_one
                else:
                    array = array_zero
            elif (oc == 'c'):
                if one < zero:
                    array = array_one
                else:
                    array = array_zero
    return int(array[0], 2)


def part_two(array):
    length_binary = len(array[0])
    oxi = filter_binary(array, length_binary, 'o')
    carb = filter_binary(array, length_binary, 'c')
    print("part two:", oxi * carb)


if (__name__ == "__main__"):
    array = open_input()
    part_one(array)
    part_two(array)
