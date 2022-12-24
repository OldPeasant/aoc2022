import sys

sys.path.append('../lib')
from pmg import *

DIRECTIONS = {
    '^' : (0, 1),
    'v' : (0, -1),
    '<' : (-1, 0),
    '>' : (1, 0)
}

BLIZZ_CHARS = set(DIRECTIONS.keys())

class Playground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blizzards = []
        self.field = Grid(width, height, " ")

    def has_blizzard(self, x, y):
        for b in self.blizzards:
            if b[1] == x and b[2] == y:
                return True
        return False

    def possible_next_pos(self, curr_positions):
        result = set()
        for p in curr_positions:
            possible_next = list(( p[0] + d[0], p[1] + d[1] ) for d in DIRECTIONS.values())
            possible_next.append(p)
            for new_p in possible_next:
                #print("    ", new_p)
                if new_p[0] >= 0 and new_p[0] < self.width and new_p[1] >= 0 and new_p[1] < self.height:
                    #print("      on border")
                    if self.field.get(*new_p) == '.' and not self.has_blizzard(*new_p):
                        #print("       That's good")
                        result.add(new_p)
                    #else:
                    #    print("       No, not good", self.field.get(*new_p) == '.', self.has_blizzard(*new_p))
                #else:
                #    print("      not on border, ignoring")
        return list(result)
    def add_field_char(self, c, x, y):
        self.field.set(x, y, c)

    def add_blizzard(self, c, x, y):
        self.blizzards.append( (c, x, y) )

    def move_blizzards(self):
        new_blizzards = []
        for b in self.blizzards:
            c, x, y = b
            inc = DIRECTIONS[c]
            new_x, new_y = x + inc[0], y + inc[1]
            #print("   move blizzard", c, "from", x, y, "to", new_x, new_y)
            if new_x == self.width - 1:
                new_x = 1
            if new_x == 0:
                new_x = self.width - 2
            if new_y == self.height - 1:
                new_y = 1
            if new_y == 0:
                new_y = self.height - 2
            #print("     after boundaries correction", new_x, new_y)
            new_blizzards.append( (c, new_x, new_y) )
        self.blizzards = new_blizzards

    def print(self):
        spots = DictOfLists()
        for b in self.blizzards:
            c, x, y = b
            spots.add("%d:%d" % (x, y), c)

        for y in range(self.height - 1, -1, -1):
            line = ""
            for x in range(self.width):
                d = spots.get("%d:%d" % (x, y))
                if len(d) == 0:
                    line += self.field.get(x, y)
                elif len(d) == 1:
                    line += d[0][0]
                else:
                    line += str(len(d))
            print(line)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    grid = Grid(len(lines[0]), len(lines))

    playground = Playground(len(lines[0]), len(lines))

    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            act_y = len(lines) - y - 1
            if c in BLIZZ_CHARS:
                playground.add_blizzard(c, x, act_y)
                playground.add_field_char('.', x, act_y)
            else:
                playground.add_field_char(c, x, act_y)
    start_pos = (lines[0].index("."), len(lines) - 1)
    end_pos = (lines[-1].index("."), 0)
    print("start pos", start_pos)
    print("end pos", end_pos)
    possible_positions = [start_pos]
    playground.print()
    i = 1
    while True:
        for p in possible_positions:
            assert(not playground.has_blizzard(*p))
        playground.move_blizzards()
        possible_positions = playground.possible_next_pos(possible_positions)
        print("-------  (1) Minute", i + 1, "-------- ", len(possible_positions))
        if end_pos in possible_positions:
            print("Reached goal after", i, "iterations")
            break
        i += 1
    i += 1
    possible_positions = [end_pos]
    while True:
        for p in possible_positions:
            assert(not playground.has_blizzard(*p))
        playground.move_blizzards()
        possible_positions = playground.possible_next_pos(possible_positions)
        print("------- (2)  Minute", i + 1, "-------- ", len(possible_positions))
        if start_pos in possible_positions:
            print("Reached start after", i, "iterations")
            break
        i += 1
    i += 1
    possible_positions = [start_pos]
    while True:
        for p in possible_positions:
            assert(not playground.has_blizzard(*p))
        playground.move_blizzards()
        possible_positions = playground.possible_next_pos(possible_positions)
        print("------- (3) Minute", i + 1, "-------- ", len(possible_positions))
        if end_pos in possible_positions:
            print("Reached goal after", i, "iterations")
            break
        i += 1
