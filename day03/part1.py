import sys

if len(sys.argv) <= 1:
    filename = "input1.txt"
else:
    filename = sys.argv[1]

def common(s1, s2):
    s = set()
    for c in s1:
        if c in s2:
            s.add(c)
    if len(s) == 1:
        for c in s:
            return c

with open(filename) as f:
    lines = f.read().splitlines()

    total = 0

    for l in lines:
        le = len(l) // 2
        r1 = l[:le]
        r2 = l[le:]
        c = common(r1, r2)
        print(c)
        o = ord(c)
        if o >96:
            v = o - 96
        else:
            v = o -64 + 26
        print(v)
        total += v
        print("----")
    print(total)
