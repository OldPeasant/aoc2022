import sys

if len(sys.argv) <= 1:
    p = "Default"
else:
    p = sys.argv[1]


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
    #print(ss)
    print(sum(ss[-3:]))
    exit(0)
    max_cal = 0
    for c in cals:
        s = sum(c)
        if s > max_cal:
            max_cal = s
    print(max_cal)
