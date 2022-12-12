import sys

sys.path.append('../lib')
from pmg import *

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

def get_neighbours(pt):
    x, y = pt
    return [ (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1) ]

def print_grid(g):
    for row in g.data:
        row_str = ''
        for c in row:
            if c is None:
                row_str += "."
            else:
                row_str +=  str(c)
        print(row_str)

def check_neighbours(inp, way, pt):
    pv = way.get_t(pt)
    nv = pv + 1
    print("check_neighbours of " + str(pt) + " (" + str(pv) + ")")
    #print_grid(way)
    for n in get_neighbours(pt):
        if way.is_inside_t(n):
            #print("  check " + str(n) + " / " + str(inp.get_t(pt)) + ", " + str(inp.get_t(n)) )
            w = way.get_t(n)
            if inp.get_t(pt) - inp.get_t(n) <= 1 and (w is None or w > nv):
                #print("yes")
                way.set_t(n, nv)
                check_neighbours(inp, way, n)
            #else:
            #    print("    no")

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    inp = Grid(len(lines[0]), len(lines))
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            inp.set(x, y, ord(c))

    start = inp.find_all(ord('S'))[0]
    end = inp.find_all(ord('E'))[0]
    print(start)
    print(end)
    inp.set_t(start, ord('a'))
    inp.set_t(end, ord('z'))
    
    way = Grid(len(lines[0]), len(lines))
    way.set_t(end, 0)

    check_neighbours(inp, way, end)
    candidates = []
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if inp.get(x, y) == ord('a'):
                w = way.get(x, y)
                if w is not None:
                #    raise Exception()
                    candidates.append(w)
    total = way.get_t(start)
    print(total)
    print(min(candidates))
