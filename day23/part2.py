import sys

sys.path.append('../lib')
from pmg import *

DELTA = {
        'N'  : (0, 1),
        'NE' : (1, 1),
        'E'  : (1, 0),
        'SE' : (1, -1),
        'S' : (0, -1),
        'SW' : (-1, -1),
        'W' : (-1, 0),
        'NW' : (-1, 1)
}

class Directions:
    def __init__(self):
        self.dirs = [
            ['N', ('N', 'NE', 'NW') ],
            ['S', ('S', 'SE', 'SW') ],
            ['W', ('W', 'NW', 'SW') ],
            ['E', ('E', 'NE', 'SE') ]
        ]
        self.index = 0

    def get_directions(self):
        directions = []
        directions.extend(self.dirs[self.index:])
        directions.extend(self.dirs[:self.index])
        return directions

    def next(self):
        self.index = (self.index + 1) % len(self.dirs)

class Playfield:
    def __init__(self, lines):
        self.grid = DictGrid('.')
        self.min_x = 99999999
        self.max_x = -99999999
        self.min_y = 99999999
        self.max_y = -99999999
        for y, l in enumerate(reversed(lines)):
            #print("read line", l)
            for x, c in enumerate(l):
                if c == '#':
                    self.set(x, y, c)
    def set(self, x, y, c):
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y
        self.grid.set(x, y, c)

    def print(self):
        print("Printing range", self.min_y, self.max_y, self.min_x, self.max_x)
        for y in range(self.max_y, self.min_y - 1, -1):
            s = ""
            for x in range(self.min_x, self.max_x + 1):
                s += self.grid.get(x, y)
            print(s)
    def count_empty(self):
        cnt = 0
        for y in range(self.max_y, self.min_y - 1, -1):
            for x in range(self.min_x, self.max_x + 1):
                if self.grid.get(x, y) == '.':
                    cnt += 1
        return cnt

def all_alone(playfield, x, y):
    for d in DELTA.values():
        if playfield.grid.get(x + d[0], y + d[1]) != '.':
            return False
    return True

def get_proposed(playfield, x, y, directions):
    #print('++++++++++++++++++++++++++++++++')
    #playfield.print()
    #print('++++++++++++++++++++++++++++++++')
    if all_alone(playfield, x, y):
        return (x, y)
    for d in directions:
        to_move, to_check = d
        #print("for", x, y, "check", to_check, "maybe move", to_move)
        all_free = True
        for c in to_check:
            next_x = x + DELTA[c][0]
            next_y = y + DELTA[c][1]
            c = playfield.grid.get(next_x, next_y)
            #print("val at", next_x, next_y, "is", c)
            if c == '#':
                all_free = False
        if all_free:
            #print("# at", x, y, "wants to move in direction", DELTA[to_move])
            return (x + DELTA[to_move][0], y + DELTA[to_move][1])
        else:
            #print("no, trying next direction")
            pass
    #print("# at", x, y, "will stay")
    return (x, y)

def do_round(orig_pf, directions):
    #print("Directions for this round", ", ".join(d[0] for d in directions))
    new_pf = Playfield([])
    proposals = {}
    
    for coord_str in orig_pf.grid.all_coords():
        x, y = coord_str #(int(c) for c in coord_str.split(':'))
        p = get_proposed(orig_pf, x, y, directions)
        #print("get propsed of", coord_str, "returned", p)
        proposals[str(coord_str[0]) + ":" + str(coord_str[1])] = str(p[0]) + ":" + str(p[1])

    prop_count = {}
    for pk, pv in proposals.items():
        #print("counting, one more", pv)
        prop_count[pv] = prop_count.get(pv, 0) + 1

    #print("Proposals")
    #print(proposals)
    #print(prop_count)
    anyone_moved = False
    for src, tgt in proposals.items():
        #print("go through src, tgt in proposals")
        #print(src)
        #print(tgt)
        if prop_count[tgt] > 1:
            new_pf.set(*(int(c) for c in src.split(':')), '#')
        elif prop_count[tgt] == 1:
            #print("CHK", src, tgt)
            if src != tgt:
                anyone_moved = True
            new_pf.set(*(int(c) for c in tgt.split(':')), '#')
        else:
            raise Exception()
    return new_pf, anyone_moved

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    directions = Directions()
    pf = Playfield(lines)
    pf.print()
    round_count = 0
    while True:
        pf, anyone_moved = do_round(pf, directions.get_directions())
        #print('====== after round', round_count + 1)
        #pf.print()
        print("Round", round_count + 1)
        directions.next()
        if not anyone_moved:
            print("done after", round_count + 1, "rounds")
            exit(0)
        round_count += 1
    print(pf.count_empty())
