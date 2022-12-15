import sys

sys.path.append('../lib')
from pmg import *

def candidates():
    for x in range(0, 4000001):
        y = 56000011 - x * 4000000
        if y >= 0 and y <= 4000000:
            print("Candidate: " + str(x) + ", " + str(y))
#candidates()
#exit(0)

def print_grid(grid):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for y in range(0, 21):
        line = ""
        for x in range(0, 21):
            v = grid.get(x, y)
            line += (v if v is not None else '.')
        print(line)
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    #interesting = 2000000
    #limit = 4000000
    interesting = 10
    limit = 20

    grid = DictGrid('.')
    lc = 0
    for l in lines:
        lc += 1
        print(lc)
        s1 = l.split(' at ')
        sensor_str = s1[1].split(':')[0]
        sensor = list([int(p.split('=')[1]) for p in sensor_str.split(", ")])
        beacon_str = s1[2]
        beacon = list([int(p.split("=")[1]) for p in beacon_str.split(", ")])
        print(sensor, beacon)
        dist = manhattan_dist(sensor, beacon)
        delta_y = abs(sensor[1] - interesting)
        remaining = dist - delta_y
        if delta_y <= interesting:
            for x in range(sensor[0] - remaining, sensor[0] + remaining + 1):
                grid.set(x, interesting, '#')
        if abs(sensor[1] - beacon[1]) <= abs(sensor[1] - interesting):
            for d in range(dist + 1):
                for p in points_at_manhattan_dist(sensor, d):
                    if not p == beacon and not p == sensor:
                        grid.set(p[0], p[1], '#')
        grid.set(sensor[0], sensor[1], 'S')
        grid.set(beacon[0], beacon[1], 'B')
    count = 0
    for c in grid.all_coords():
        if c[1] == interesting and grid.get(c[0], c[1]) == '#':
            count += 1
    print_grid(grid)
    print(count)
