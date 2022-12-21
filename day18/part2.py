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

def neighbours(x, y, z):
    neigh = []
    for s in sides:
        neigh.append( (x + s[0], y + s[1], z + s[2]))
    return neigh

def is_free(g, x, y, z):
    bubble = DictGrid3D()
    
    for s in sides:
        if not g.get(x + s[0], y + s[1], z + s[2]):
            return True
    return False

def cube_sides(min_x, max_x, min_y, max_y, min_z, max_z):
    cs = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if x == min_x or x == max_x or y == min_y or y == max_y or z == min_z or z == max_z:
                    cs.append( (x, y, z) )
    return cs

#for cs in cube_sides(1, 3, 1, 3, 1, 6):
#    print(cs)
#exit(0)
def calc_free_bubbles_inside(g, free, min_x, max_x, min_y, max_y, min_z, max_z):
    #print("cfbi", min_x, max_x, min_y, max_y, min_z, max_z)
    found_one = False
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if not g.get(x, y, z) and not free.get(x, y, z):
                    for n in neighbours(x, y, z):
                        if free.get(*n):
                            free.set(x, y, z, True)
                            found_one = True
    return found_one

def calc_free_bubbles(g, free, min_x, max_x, min_y, max_y, min_z, max_z):
    for s in cube_sides(min_x, max_x, min_y, max_y, min_z, max_z):
#        print("setting free init", s)
        free.set(*s, True)
    while True:
        if not calc_free_bubbles_inside(g, free, min_x+1, max_x-1, min_y+1,max_y-1, min_z+1, max_z-1):
            return


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
    print(min_x, max_x, min_y, max_y, min_z, max_z)
    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1
    free = DictGrid3D()
    calc_free_bubbles(g, free, min_x, max_x, min_y, max_y, min_z, max_z)

    for f in free.all_coords():
#        print(g.get(*f))
#        print(free.get(*f))
        print("Free", f)
#        if g.get(*f):
#            raise Exception("free but occupied: %s" % str(f))
    count_free = 0
    for c in g.all_coords():
        for n in neighbours(*c):
            if free.get(*n):
                count_free += 1
    print(min_x, max_x, min_y, max_y, min_z, max_z)
    print(count_free)
