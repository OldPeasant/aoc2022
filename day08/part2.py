import sys

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]

def score_dir(forrest, x, y, direction):
    score = 0
    h = forrest[x][y]
    while x > 0 and x < len(forrest) - 1 and y > 0 and y < len(forrest[x]) - 1:
        x += direction[0]
        y += direction[1]
        score += 1
        if forrest[x][y] >= h:
            break
    return score

def score(forrest, x, y):
    total_score = 1
    for direction in [ (0, 1), (0, -1), (1, 0), (-1, 0) ]:
        total_score *= score_dir(forrest, x, y, direction)
    return total_score

with open(filename) as f:
    lines = f.read().splitlines()

    forrest = []
    for l in lines:
        forrest.append(list([int(h) for h in l]))
    max_score = 0
    for y in range(len(forrest)):
        row = forrest[y]
        for x in range(len(row)):
            s = score(forrest, x, y)
            if s > max_score:
                max_score = s
    print(max_score)
