import sys

sys.path.append('../lib')
from pmg import *

def split_seg(seg, range_to_remove):
    #print("split_seg", seg, range_to_remove)
    if seg[1] < range_to_remove[0]:
        #print("    seg is below range_to_remove: keep it")
        return [seg]
    if seg[0] > range_to_remove[1]:
        #print("    seg is above range_to_remove: keep it")
        return [seg]
    if seg[0] > range_to_remove[0] and seg[1] < range_to_remove[1]:
        #print("    seg is inside range_to_remove: discard it")
        return []
    part1 = (seg[0], range_to_remove[0] - 1)
    part2 = (range_to_remove[1] + 1, seg[1])
    #print(" split_seg parts", part1, part2)
    result = list([p for p in [part1, part2] if p[1] >= p[0]]) 
    #print("after split_seg: ", result)
    return result

def remove(parts, range_to_remove):
    #print()
    #print("remove", parts, range_to_remove)
    remaining = []
    for p in parts:
        #print("  gonna split_seg part ", p, 'by', range_to_remove)
        remaining.extend(split_seg(p, range_to_remove))
    #print("  remaining", remaining)
    return remaining

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    limit = 4000000
    #limit = 20
    
    maybe = []
    for i in range(limit + 1):
        maybe.append( [(0, limit)] )

    print("let's go")
    lc = 0
    for l in lines:
        lc += 1
        print("input line no", lc)
        s1 = l.split(' at ')
        sensor_str = s1[1].split(':')[0]
        sensor = list([int(p.split('=')[1]) for p in sensor_str.split(", ")])
        beacon_str = s1[2]
        beacon = list([int(p.split("=")[1]) for p in beacon_str.split(", ")])
        dist = manhattan_dist(sensor, beacon)
        #print("sensor, beacon, dist", sensor, beacon, dist)
        y_min = max(0, sensor[1] - dist) 
        y_max = min(limit, sensor[1] + dist)
        #print("y min max", y_min, y_max)
        for y in range(y_min, y_max + 1):
            #print("doing y", y)
            delta_y = abs(sensor[1] - y)
            delta_x = abs(dist - delta_y)
            to_remove = (sensor[0] - delta_x, sensor[0] + delta_x)
            row = maybe[y]
            #print("row at y=" + str(y), 'before',  row)
            #print("****************************")
            #print(row)
            #print("****************************")
            maybe[y] = remove(row, to_remove)
            #print("row at y=" + str(y), 'after',  maybe[y])
        #print('------------------------')
        #for y in range(0, limit + 1):
        #    if len(maybe[y]) > 0:
        #        print("y=" + str(y), maybe[y])
        #print('------------------------')




print('------------------------')
for y in range(0, limit + 1):
    if len(maybe[y]) > 0:
        print(y, maybe[y])
        for m in maybe[y]:
            if m[0] != m[1]:
                raise Exception()
            x = m[0]
            print("result+ " + str(x * limit + y))
print('------------------------')
