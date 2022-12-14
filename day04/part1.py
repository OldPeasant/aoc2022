import sys

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]

def parse_range(r):
    return list(int(i) for i in r.split('-'))

def full_overlap(r1, r2):
    if r1[0] >= r2[0] and r1[1] <= r2[1]:
        return True
    if r2[0] >= r1[0] and r2[1] <= r1[1]:
        return True
    return False

with open(filename) as f:
    lines = f.read().splitlines()

    count = 0
    for l in lines:
        parts = l.split(',')
        r1 = parse_range(parts[0])
        r2 = parse_range(parts[1])
        if full_overlap(r1, r2):
            count += 1
    print(count)
