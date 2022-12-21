import sys

sys.path.append('../lib')
from pmg import *

sides = [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1)
]

def is_free(g, x, y, z):
    bubble = DictGrid3D()
    
    for s in sides:
        if not g.get(x + s[0], y + s[1], z + s[2]):
            return True
    return False

def calc_free_bubbles(g, min_x, max_x, min_y, max_y, min_z, max_z):
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_y

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    g = DictGrid3D()

    for l in lines:
        x, y, z = list(int(n) for n in l.split(','))
        g.set(x, y, z, True)
    min_x, min_y, min_z, max_x, max_y, max_z = 9999,9999,9999,-9999,-9999,-9999
    for c in g.all_coords():
        if c[0] < min_x:
            min_x = c[0]
        if c[0] > max_x:
            max_x = c[0]
        if c[1] < min_y:
            min_y = c[1]
        if c[1] > max_y:
            max_y = c[1]
        if c[2] < min_z:
            min_z = c[2]
        if c[2] > max_z:
            max_z = c[2]
    f = calc_free_bubbles(g)
    count_free = 0
    for c in g.all_coords():
        for s in sides:
            air =  (c[0] + s[0], c[1] + s[1], c[2] + s[2])
            if not g.get(*air):
                if is_free(g, *air):
                    count_free += 1
    print(min_x, max_x, min_y, max_y, min_z, max_z)
    print(count_free)
