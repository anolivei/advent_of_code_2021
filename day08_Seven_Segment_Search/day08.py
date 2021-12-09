from collections import defaultdict


def open_input():
    with open("input.txt") as fd:
        array = [i.split(" | ") for i in fd.read().splitlines()]
    array = [(signal.split(), output.split()) for signal, output in array]
    return array


def part_one(array):
    dictionary = defaultdict(int)
    for signal, output in array:
        for i in output:
            dictionary[len(i)] += 1
    one = dictionary[2]
    four = dictionary[4]
    seven = dictionary[3]
    eight = dictionary[7]
    print("part one:", one + four + seven + eight)


def part_two(array):
    ret = 0
    for signal, output in array:
        length = [len(i) for i in signal]
        known = [None] * 10
        known[1] = signal[length.index(2)]
        known[4] = signal[length.index(4)]
        known[7] = signal[length.index(3)]
        known[8] = signal[length.index(7)]
        for unknown in signal:
            if len(unknown) == 5:
                if len(set(known[7]) & set(unknown)) == 3:
                    known[3] = unknown
                elif len(set(known[4]) & set(unknown)) == 2:
                    known[2] = unknown
                else:
                    known[5] = unknown
            elif len(unknown) == 6:
                if len(set(known[4]) & set(unknown)) == 4:
                    known[9] = unknown
                elif len(set(known[7]) & set(unknown)) == 3:
                    known[0] = unknown
                else:
                    known[6] = unknown
        known = [sorted(i) for i in known]
        output = [sorted(i) for i in output]
        ret += int("".join(str(known.index(i)) for i in output))
    print("part two:", ret)


if (__name__ == "__main__"):
    array = open_input()
    part_one(array)
    part_two(array)
