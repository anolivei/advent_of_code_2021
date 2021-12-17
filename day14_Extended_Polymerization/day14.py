from collections import defaultdict, Counter


class Data():
    with open("input.txt") as fd:
        data = [i.split(" -> ") for i in fd.read().splitlines()]

    template = data[0][0]

    insertion = defaultdict(str)
    for d in data[2:]:
        insertion[d[0]] = d[1]

    pairs = []
    for i in range(len(template) - 1):
        pairs.append(template[i:i + 2])
    pairs = Counter(pairs)


def solution(Data):
    pairs = Data.pairs
    template = Data.template
    insertion = Data.insertion

    for i in range(1, 41):
        new_pairs = Counter()
        for pair, num in pairs.items():
            new_pairs[pair[0] + insertion[pair]] += num
            new_pairs[insertion[pair] + pair[1]] += num
        pairs = new_pairs
        if i in (10, 40):
            letters = Counter()
            for pair, num in pairs.items():
                letters[pair[0]] += num
            letters[template[-1]] += 1
            ret = max(letters.values()) - min(letters.values())
            if (i == 10):
                print("part one:", ret)
            else:
                print("part two:", ret)


if (__name__ == "__main__"):
    solution(Data)
