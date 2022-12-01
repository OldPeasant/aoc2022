import sys

with open("input2.txt") as f:
    lines = f.read().splitlines()

    cals = []
    curr = []
    for l in lines:
        if len(l.strip()) == 0:
            cals.append(curr)
            curr = []
        else:
            curr.append(int(l))
    if len(curr) > 0:
        cals.append(curr)

    sums = list(sum(c) for c in cals)
    ss = sorted(sums)
    print(sum(sorted(sums)[-3:]))
