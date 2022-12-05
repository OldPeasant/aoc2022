import sys

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]

def extract_move(line):
    parts = line.split(" ")
    return (int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1)

with open(filename) as f:
    lines = f.read().splitlines()
    
    grid_lines = []
    move_lines = []
    mode_grid = True
    for l in lines:
        if mode_grid:
            if len(l.strip()) == 0:
                mode_grid = False
            else:
                grid_lines.append(l)
        else:
            move_lines.append(l)
    grid_lines.reverse()
    chunks = grid_lines[1].split(" ")
    stacks = list([] for l in chunks)
    print(stacks)
    for row in grid_lines[1:]:
        ix = 0
        col = 0
        while ix <= len(row):
            bl = row[ix:ix+3]
            print(str(ix) + "  *" + bl + "*")
            if len(bl.strip()) > 0:
                stacks[col].append(bl[1])
            ix += 4
            col += 1
    print(stacks)
    for m in move_lines:
        count, col_from, col_to = extract_move(m)
        print("Move", count, col_from, col_to)
        stacks[col_to].extend(stacks[col_from][-count:])
        for i in range(count):
            stacks[col_from].pop()
        print(stacks)
    print("".join(c.pop() for c in stacks))
