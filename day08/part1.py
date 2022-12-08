import sys

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]

def is_visible_dir(forrest, x, y, direction):
    h = forrest[x][y]
    while x > 0 and x < len(forrest) - 1 and y > 0 and y < len(forrest[x]) - 1:
        x += direction[0]
        y += direction[1]
        if forrest[x][y] >= h:
            return False
    return True

def is_visible(forrest, x, y):
    for direction in [ (0, 1), (0, -1), (1, 0), (-1, 0) ]:
        if is_visible_dir(forrest, x, y, direction):
            return True
    return False

with open(filename) as f:
    lines = f.read().splitlines()

    forrest = []
    for l in lines:
        forrest.append(list([int(h) for h in l]))
    visible_count = 0
    for y in range(len(forrest)):
        row = forrest[y]
        for x in range(len(row)):
            if is_visible(forrest, x, y):
                visible_count += 1
    print(visible_count)
