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
    return list(s)

def only(l):
    if len(l) == 1:
        for c in l:
            return c

def process(lines):
    c = only(common(lines[0], common(lines[1], lines[2])))
    
    o = ord(c)
    if o >96:
        v = o - 96
    else:
        v = o -64 + 26
    return v

with open(filename) as f:
    lines = f.read().splitlines()

    total = 0
    ix = 0
    while ix < len(lines):
        v = process(lines[ix:ix+3])
        total += v
        ix += 3
    print(total)

