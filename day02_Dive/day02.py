def open_input():
    with open("input.txt") as fd:
        dictionary = fd.read().splitlines()
        fd.close()
    return dictionary


def part_one(dictionary):
    print("part one:", dictionary)


def part_two(dictionary):
    print("part two:", dictionary)


if (__name__ == "__main__"):
    dictionary = open_input()
    part_one(dictionary)
    part_two(dictionary)
