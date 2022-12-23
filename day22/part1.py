import sys

sys.path.append('../lib')
from pmg import *

# facing
# 0 right
# 1 down
# 2 left
# 3 up
NEXT_FACING = {
        0 : { 'L' : 3, 'R' : 1},
        1 : { 'L' : 0, 'R' : 2},
        2 : { 'L' : 1, 'R' : 3},
        3 : { 'L' : 2, 'R' : 0}
}

NEXT_TILE_DELTA = { 0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1) }


class Walker:
    def __init__(self, grid, width, height):
        self.grid = grid
        self.width = width
        self.height = height
        self.pos = self.find_start_pos()
        self.direction = 0

    def find_start_pos(self):
        y = height - 1
        x = 0
        while grid.get(x, y) != '.':
            x += 1
        print("start position", x, y)
        return (x, y)

    def normalize(self, r):
        if r[0] >= self.width:
            r = (0, r[1])
        if r[0] < 0:
            r = (self.width - 1, r[1])
        if r[1] >= self.height:
            r = (r[0], 0)
        if r[1] < 0:
            r = (r[0], self.height - 1)
        return r

    def next_char(self, p, inc):
        actual_count = 0
        while True:
            p = self.normalize((p[0] + inc[0], p[1] + inc[1]))
            c = self.grid.get(*p)
            actual_count += 1
            if c == '#' or c == '.':
                return c, actual_count

    def move(self, inc, max_count):
        print("move", self.pos, inc, max_count)
        count = 0
        while count < max_count:
            c, actual_count = self.next_char(self.pos, inc)
            if c == '#':
                print("  found # after", count, "moves")
                return
            print("  moved", count, "char is", c)
            self.pos = self.normalize( (self.pos[0] + actual_count * inc[0], self.pos[1] + actual_count * inc[1]) )
            count += 1

    def move_in_direction(self, count):
        inc = NEXT_TILE_DELTA[self.direction]
        self.move(inc, count)
        print(" have moved to", self.pos)

    def make_move(self, move):
        if move[0] == 'move':
            self.move_in_direction(move[1])
            print("moving in direction", self.direction, "done, now at", self.pos)
        elif move[0] == 'rotate':
            self.direction = NEXT_FACING[self.direction][move[1]]
            print("rotated to", self.direction)
        else:
            raise Exception(str(move))

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    grid = DictGrid()
    width = -1
    height = -1
    h = 0
    for l in reversed(lines[:-2]):
        if len(l) == 0:
            break
        w = 0
        for c in l:
            grid.set(w, h, c)
            print("have put a", c, "at", w, h)
            w += 1
        if w > width:
            width = w
        h += 1
    height = h
    for y in range(height, -1, -1):
        row = ""
        for x in range(width + 1):
            c = grid.get(x, y)
            if c is None:
                c = ' '
            row += c
        print(row)
    print("Grid size", width, height)
    grouper = Grouper()
    for c in lines[-1]:
        if not c.isnumeric():
            grouper.next()
        grouper.add(c)
        if not c.isnumeric():
            grouper.next()

    moves = []
    next_is_number = True
    for g in grouper.groups:
        if next_is_number:
            moves.append(['move', int("".join(g))])
        else:
            moves.append(['rotate', g[0]])
        next_is_number = not next_is_number
    w = Walker(grid, width, height)
    for m in moves:
        print("make move:", m)
        w.make_move(m)

    base_1_x = w.pos[0] + 1
    base_1_y = height - w.pos[1] 
    print(base_1_x)
    print(base_1_y)
    print(w.direction)
    solution = 1000 * base_1_y + 4 * base_1_x + w.direction
    print(solution)
