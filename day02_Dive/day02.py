def open_input():
    with open("input.txt") as fd:
        array = fd.read().splitlines()
        fd.close()
    return array


def make_dictionary(array):
    dictionary = {"up": [], "down": [], "forward": []}
    lenght = len(array)
    for i in range(0, lenght):
        array[i] = array[i].split(' ')
        if array[i][0] == "up":
            dictionary["up"].append(int(array[i][1]))
        elif array[i][0] == "down":
            dictionary["down"].append(int(array[i][1]))
        elif array[i][0] == "forward":
            dictionary["forward"].append(int(array[i][1]))
    return dictionary


def part_one(array):
    dictionary = make_dictionary(array)
    up = sum(dictionary["up"])
    down = sum(dictionary["down"])
    forward = sum(dictionary["forward"])
    print("part one:", (down - up) * forward)


def part_two(array):
    aim = 0
    ver = 0
    hor = 0
    lenght = len(array)
    for i in range(0, lenght):
        if array[i][0] == "up":
            aim -= int(array[i][1])
        elif array[i][0] == "down":
            aim += int(array[i][1])
        elif array[i][0] == "forward":
            hor += int(array[i][1])
            ver += int(array[i][1]) * aim
    print("part two:", ver * hor)


if (__name__ == "__main__"):
    array = open_input()
    part_one(array)
    part_two(array)
