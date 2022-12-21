import sys

sys.path.append('../lib')
from pmg import *

class JetStream:
    def __init__(self, inp):
        self.jets = []
        for c in inp:
            if c == '>':
                self.jets.append(1)
            elif c == '<':
                self.jets.append(-1)
            else:
                raise Exception(c)
        self.pos = 0

    def next(self):
        j = self.jets[self.pos]
        self.pos += 1
        if self.pos == len(self.jets):
            self.pos = 0
        return j

class Rock:
    def __init__(self, width, height, pattern):
        self.width = width
        self.height = height
        self.pattern = pattern

class RockStream:
    def __init__(self):
        self.rocks = [
            Rock(4, 1, ['####']),
            Rock(3, 3, [' # ', '###', ' # ']),
            Rock(3, 3, ['  #', '  #', '###']),
            Rock(1, 4, ['#', '#', '#', '#']),
            Rock(2, 2, ['##', '##'])
        ]
        self.pos = 0

    def next(self):
        r = self.rocks[self.pos]
        self.pos += 1
        if self.pos == len(self.rocks):
            self.pos = 0
        return r

class Cave:
    def __init__(self):
        self.stones = []
        self.highest_rock = -1

    def _grow_to_y(self, y):
        while y >= len(self.stones):
            self.stones.append(['.','.','.','.','.','.','.'])

    def has_stone(self, x, y):
        #print("check has stone", x, y)
        self._grow_to_y(y)
        if x < 0 or x > 6:
            #print("  true, x is %d" % x)
            return True
        if y < 0:
            #print("  true, y is %d" % y)
            return True
        #print('  element at %d, %d is %s' % (x, y, self.stones[y][x]))
        return self.stones[y][x] == '#'

    def can_be_at(self, rock, x, y):
        #print("can_be_at", x, y)
        for dx in range(rock.width):
            for dy in range(rock.height):
                if rock.pattern[dy][dx] == '#' and self.has_stone(x + dx, y - dy):
                    return False
        return True

    def solidify(self, rock, x, y):
        print("solidify at %d, %d" % (x, y))
        for dx in range(rock.width):
            for dy in range(rock.height):
                if rock.pattern[dy][dx] == '#':
                    #print("assert", x, y, dx, dy, x+dx, y-dy, flush=True)
                    assert(not self.has_stone(x + dx, y - dy))
                    self.stones[y - dy][x + dx] = '#'
        self.highest_rock = max(self.highest_rock, y)

    def print(self):
        print("highest rock at %d" % self.highest_rock)
        for i, l in enumerate(reversed(self.stones)):
            print(''.join(l) + '  ' + str(len(self.stones) - i - 1))

    def print_with_rock_at(self, rock, rx, ry):
        print("- - - - - - - - - %d" % self.highest_rock)
        for y in range(ry + 1, -1, -1):
            if y >= len(self.stones):
                cave_line = ['.','.','.','.','.','.','.']
            else:
                cave_line = list(self.stones[y])
            dr = ry - y
            if dr >= 0 and dr < rock.height:
                for dx in range(rock.width):
                    x = rx + dx
                    if rock.pattern[dr][dx] == '#':
                        cave_line[x] = '@'
            print("".join(cave_line) + "  " + str(y))
        print("-=-=-=-=-=-=-=-=-")


def fall(cave, jet_stream, rock, x, y):
    while True:
        #print(" falling", x, y)
        assert(cave.can_be_at(rock, x, y))
        js = jet_stream.next()
        new_x = x + js
        if cave.can_be_at(rock, new_x, y):
            #print("   jet pushes rock %s" % ("left" if js < 0 else "right"))
            x = new_x
        else:
            #print("   can't move to x %d, staying at %d" % (new_x, x))
            pass
        #cave.print_with_rock_at(rock, x, y)
        new_y = y - 1
        if cave.can_be_at(rock, x, new_y):
            y = new_y
            #print("   rock falls 1 unit")
            #cave.print_with_rock_at(rock, x, y)
        else:
            #cave.print_with_rock_at(rock, x, y)
            #print("   can't fall further down, solidify at %d, %d" % (x, y))
            cave.solidify(rock, x, y)
            return

with open(sys.argv[1]) as f:
    jet_stream = JetStream(f.read().splitlines()[0])
    rock_stream = RockStream()

    cave = Cave()
    for i in range(2022):
        rock = rock_stream.next()
        print("Rock no %d" % i)
        start_x = 2
        start_y = cave.highest_rock + 3 + rock.height
        #print("before falling", cave.highest_rock, rock.height)
        #print('****************')
        #cave.print()
        #print('----------------')
        #cave.print_with_rock_at(rock, start_x, start_y)
        #print('----------------')
        fall(cave, jet_stream, rock, start_x, start_y)
        #cave.print()

    print('=============================')
    print(cave.highest_rock + 1)
