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

SIDES = {
        "1:0" : 5,
        "2:0" : 6,
        "1:1" : 4,
        "0:2" : 2,
        "1:2" : 3,
        "0:3" : 1
}

class WalkerBak:
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

    def remains_inside(self, px, py, inc):
        nx = px + inc[0]
        ny = py + inc[1]
        return nx >=0 and ny >= 0 and nx < self.width / 3 and ny < self.height / 3

    def determine_next(self, p, inc):
        rel_x, rel_y = p[0] % 50, p[1] % 50
        if this.remains_inside(rel_x, rel_y, inc):
            return p[0] + inc[0], p[1] + inc[1]
        side_coord = (p[0] // 50, p[1] // 50)
        side = SIDES[str(side_coord[0]) + ":" + str(side_coord[1])]
        
        if side == 1:
            return determine_next_side_1
        if inc[0] == 1:
            # move right
            if side == 1:
                bla
            elif side == 2:
                bla
            elif side == 3:
                bla
            elif side == 4:
                bla
            elif side == 5:
                bla
            elif side == 6:
                bla
            else:
                raise Exception()
        elif inc[0] == -1:
            # move left
            if side == 1:
                bla
            elif side == 2:
                bla
            elif side == 3:
                bla
            elif side == 4:
                bla
            elif side == 5:
                bla
            elif side == 6:
                bla
            else:
                raise Exception()

        elif inc[1] == 1:
            # move up
            if side == 1:
                bla
            elif side == 2:
                bla
            elif side == 3:
                bla
            elif side == 4:
                bla
            elif side == 5:
                bla
            elif side == 6:
                bla
            else:
                raise Exception()

        elif inc[1] == -1:
            if side == 1:
                bla
            elif side == 2:
                bla
            elif side == 3:
                bla
            elif side == 4:
                bla
            elif side == 5:
                bla
            elif side == 6:
                bla
            else:
                raise Exception()
            # move down

        else:
            raise Exception()

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
            print("rotated to", self.direction)
        else:
            raise Exception(str(move))



GRID_COORDS = {
    1: (0, 0),
    2: (0, 50),
    3: (1, 50),
    4: (1, 100),
    5: (1, 150),
    6: (2, 150)
}


class Walker:
    def __init__(self, grids, start_pos, facing):
        self.grids = grids
        self.pos = start_pos
        self.facing = facing

    def leave_left(self, grid_no, y):
        if grid_no == 1:
            return ([5, (49-y, 49)], 1)
        elif grid_no == 2:
            return ([5, (0, 49-y)], 0)
        elif grid_no == 3:
            return ([2, (49, y)], 2)
        elif grid_no == 4:
            return ([2, (49 - y, 49)], 1)
        elif grid_no == 5:
            return ([2, (0, 49 - y)], 0)
        elif grid_no == 6:
            return ([5, (49, y)], 2)
        else:
            raise Exception()
    def leave_right(self, grid_no, y):
        if grid_no == 1:
            return ([3, (49 - y, 0)], 3)
        elif grid_no == 2:
            return ([3, (0, y)], 0)
        elif grid_no == 3:
            return ([6, (49, 49 - y)], 2)
        elif grid_no == 4:
            return ([6, (49 - y, 0)], 3)
        elif grid_no == 5:
            return ([6, (0, y)], 0)
        elif grid_no == 6:
            return ([3, (49, 49 - y)], 2)
        else:
            raise Exception()

    def leave_top(self, grid_no, x):
        if grid_no == 1:
            return ([2, (x, 0)], 3)
        elif grid_no == 2:
            return ([4, (0, 49 - x)], 0)
        elif grid_no == 3:
            return ([4, (x, 0)], 3)
        elif grid_no == 4:
            return ([5, (x, 0)], 3)
        elif grid_no == 5:
            return ([1, (0, 49 - x)], 0)
        elif grid_no == 6:
            return ([1, (x, 0)], 3)
        else:
            raise Exception()

    def leave_bottom(self, grid_no, x):
        if grid_no == 1:
            return ([6, (x, 49)], 1)
        elif grid_no == 2:
            return ([1, (x, 49)], 1)
        elif grid_no == 3:
            return ([1, (49, 49 - x)], 2)
        elif grid_no == 4:
            return ([3, (x, 49)], 1)
        elif grid_no == 5:
            return ([4, (x, 49)], 1)
        elif grid_no == 6:
            return ([4, (49, 49 - x)], 2)
        else:
            raise Exception()

    def find_next(self):
        grid_no = self.pos[0]
        rel_coord = self.pos[1]
        delta = NEXT_TILE_DELTA[self.facing]
        nc = (rel_coord[0] + delta[0], rel_coord[1] + delta[1])
        print("find_next", grid_no, rel_coord, delta, nc)
        if nc[0] < 0:
            return self.leave_left(grid_no, rel_coord[1])
        elif nc[0] >= 50:
            return self.leave_right(grid_no, rel_coord[1])
        elif nc[1] < 0:
            return self.leave_bottom(grid_no, rel_coord[0])
        elif nc[1] >= 50:
            return self.leave_top(grid_no, rel_coord[0])
        else:
            return ([grid_no, nc], self.facing)

    def move_one(self):
        next_pos, next_facing = self.find_next()
        c = self.grids[next_pos[0]].get(*next_pos[1])
        if c == '#':
            # don't move, it's blocked
            pass
        elif c == '.':
            self.pos = next_pos
            self.facing = next_facing
        else:
            raise Exception()

    def make_move(self, move):
        print("make_move", move)
        if move[0] == 'move':
            for i in range(move[1]):
                self.move_one()
        elif move[0] == 'rotate':
            self.facing = NEXT_FACING[self.facing][move[1]]
        else:
            raise Exception()


SIDE_COORDS = {
        1: (0, 0),
        2: (0, 1),
        3: (1, 1),
        4: (1, 2),
        5: (1, 3),
        6: (2, 3)
}

def read_side_grid(lines, sc):
    print("read_side_grid", sc)
    g = Grid(50, 50)
    for y in range(50):
        for x in range(50):
            print("x", x, "y", y)
            row_coord = sc[1] * 50 + y
            col_coord = sc[0] * 50 + x
            print("row_coord", row_coord, "col_coord", col_coord)
            g.set(x, y, lines[row_coord][col_coord])
            assert(g.get(x, y) is not None)
    return g

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    grid_lines = list(reversed(lines[:-2]))
    side_grids = {}
    for s, sc in SIDE_COORDS.items():
        side_grids[s] = read_side_grid(grid_lines, sc)
    start_pos = [5, (0, 49)]
    facing = 0

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

    w = Walker(side_grids, start_pos, facing)
    for m in moves:
        print("make move:", m)
        w.make_move(m)

    pos = w.pos
    x = GRID_COORDS[pos[0]][0] + pos[1][0]
    y = GRID_COORDS[pos[0]][1] + pos[1][1]
    print("x, y", x, y)
    base_1_x = x + 1
    base_1_y = len(grid_lines) - y
    print(base_1_x)
    print(base_1_y)
    print(w.facing)
    solution = 1000 * base_1_y + 4 * base_1_x + w.facing
    print(solution)
