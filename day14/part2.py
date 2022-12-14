import sys

sys.path.append('../lib')
from pmg import *

def print_grid(grid):
    print("- - - - - - - - - - -")
    print(grid.data)
    for y in range (-1, 30, 1):
        line = ""
        for x in range (480, 520):
            v = grid.get(x, y)
            line += v if v is not None else " "
        print("> " + line + " <")
grid = DictGrid()
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    max_y = -9999999999999
    for l in lines:
        str_coords = l.split(' -> ')
        coords = []
        for sc in str_coords:
            c = sc.split(",")
            coords.append( (int(c[0]), int(c[1])) )
        m = max( c[1] for c in coords )
        if m > max_y:
            max_y = m
        for i in range(0, len(coords)  - 1):
            start = coords[i]
            end = coords[i + 1]
            if start[0] == end[0]:
                delta = sig(end[1] - start[1]) 
                for y in range(start[1], end[1] + delta, delta):
                    grid.set(start[0], y, "#")
            elif start[1] == end[1]:
                delta = sig(end[0] - start[0])
                for x in range(start[0], end[0] + delta, delta):
                    grid.set(x, start[1], "#")
            else:
                raise Exception()
    for x in range(-3* max_y, 500 + 3 * max_y):
        grid.set(x, max_y + 2, "#")
    print_grid(grid)
    source = (500, 0)
    count_sand = 0
    while True:
        px = source[0]
        py = source[1]
        while True:
            if grid.get(px, py + 1) is None:
                py = py + 1
            elif grid.get(px - 1, py + 1) is None:
                px = px - 1
                py = py + 1
            elif grid.get(px + 1, py + 1) is None:
                px = px + 1
                py = py + 1
            else:
                if grid.get(px, py) == 'O':
                    print(count_sand)
                    exit(1)
                grid.set(px, py, 'O')
                break
            #if py > max_y:
            #    print(count_sand)
            #    exit(0)
        #print_grid(grid)
        count_sand += 1

