# 1310

def open_input():
    with open("input_test.txt") as fd:
        array = [i.split(",") for i in fd.read().splitlines()]
    return array


def ft_points(array):
    i = 0
    while array[i] != ['']:
        i += 1
    points = array[:i]
    points = [(int(x), int(y)) for x, y in points]
    return points


def ft_instructions(array):
    instructions = []
    i = 0
    while array[i] != ['']:
        i += 1
    i += 1
    instructions = array[i:]
    return instructions


def part_one():
    print("part one:")


def part_two():
    print("part two:")


if (__name__ == "__main__"):
    array = open_input()
    points = ft_points(array)
    instructions = ft_instructions(array)
    print(f"{array}\n\n{points}\n\n{instructions}")
    part_one()
    part_two()
