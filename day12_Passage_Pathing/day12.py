from collections import defaultdict, Counter


def open_input():
    with open("input.txt") as fd:
        array = [i.split("-") for i in fd.read().splitlines()]
    array = [(x, y) for x, y in array]
    return array


def check_point(path, cave):
    cavecounts = Counter(path)
    if cave == 'start':
        return False
    if cave.isupper() or cave not in cavecounts:
        return True
    for k in cavecounts.keys():
        if k.islower() and cavecounts[k] == 2:
            return False


def solution(part):
    tuples = open_input()
    dictionary = defaultdict(lambda: [])
    for x, y in tuples:
        dictionary[x].append(y)
        dictionary[y].append(x)
    paths = set()
    start = [['start']]
    for path in start:
        if path[-1] == 'end':
            paths.add(tuple(path))
            continue
        for cave in dictionary[path[-1]]:
            if (
                (part == "one" and cave.islower() and cave in path) or
                (part == "two" and check_point(path, cave) is False)
            ):
                continue
            start.append(path + [cave])
    return len(paths)


def part_one():
    ret = solution("one")
    print("part one:", ret)


def part_two():
    ret = solution("two")
    print("part two:", ret)


if (__name__ == "__main__"):
    part_one()
    part_two()
