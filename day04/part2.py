import sys

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]

def parse_range(r):
    return list(int(i) for i in r.split('-'))

def inrange(val, rng):
    return val >= rng[0] and val <= rng[1]

def overlap(r1, r2):
    return inrange(r1[0], r2) or inrange(r1[1], r2) or inrange(r2[0], r1) or inrange(r2[1], r1)

with open(filename) as f:
    lines = f.read().splitlines()

    count = 0
    for l in lines:
        parts = l.split(',')
        r1 = parse_range(parts[0])
        r2 = parse_range(parts[1])
        if overlap(r1, r2):
            count += 1
    print(count)
