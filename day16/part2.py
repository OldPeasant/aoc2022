import sys

sys.path.append('../lib')
from pmg import *

valves = {}
non_zero_valves = []

class Valve:
    def __init__(self, name, flow, next_valves):
        self.name = name
        self.flow = flow
        self.next_valves = next_valves
        self.is_open = False
        self.max_visits = len(next_valves)

    def possible_actions(self):
        actions = []
        if not self.is_open and self.flow > 0:
            actions.append(['open'])
        for n in self.next_valves:
            actions.append(['move', n])
        return actions

    def __repr__(self):
        return "Valve[%s, %d, %s]" % (self.name, self.flow, "/".join(v for v in self.next_valves))

class Distances:
    def __init__(self):
        self.dist = {}

    def set_dist(self, a, b, d):
        if a > b:
            self.set_dist(b, a, d)
            return
        if a not in self.dist:
            self.dist[a] = {}
        dist_a = self.dist[a]
        if b in dist_a:
            if dist_a[b] == d:
                return
            else:
                raise Exception("Dist %s -> %s already set (%d)" % (a, b, dist_a[b]))
        dist_a[b] = d
    
    def get_dist(self, a, b):
        if a > b:
            return self.get_dist(b, a)
        if a not in self.dist:
            return None
        dist_a = self.dist[a]
        if b not in dist_a:
            return None
        return dist_a[b]
 
distances = Distances()

def parse_valve(line):
    by_space = line.split(' ')
    name = by_space[1]
    flow = int(by_space[4].split('=')[1].split(';')[0])
    if "to valves " in line:
        next_valves = line.split("to valves ")[1].split(", ")
    elif "to valve " in line:
        next_valves = line.split("to valve ")[1].split(", ")
    else:
        raise Exception()
    return Valve(name, flow, next_valves)

def calc_all_distances():
    global valves, distances
    while True:
        found = False
        for v1 in valves.values():
            for v2 in valves.values():
                print("  checking", v1.name, v2.name)
                if distances.get_dist(v1.name, v2.name) is not None:
                    continue
                if v1.name != v2.name and distances.get_dist(v1.name, v2.name) is None:
                    min_d = 99999999
                    actually_found = False
                    for n in v1.next_valves:
                        ex_d = distances.get_dist(n, v2.name)
                        if ex_d is not None:
                            new_1_2 = ex_d + 1
                            if new_1_2 < min_d:
                                min_d = new_1_2
                                actually_found = True
                    if actually_found:
                        distances.set_dist(v1.name, v2.name, min_d)
                        print("Have set dist", v1.name, v2.name, min_d)
                    found = True
        if not found:
            return

def print_distances():
    global valves, distances
    for v1 in valves.values():
        for v2 in valves.values():
            print("Distance", v1.name, v2.name, distances.get_dist(v1.name, v2.name))

best_score = -1

def examine(sequence, non_zero_names, score, t):
    global best_score
    print("examine", sequence, non_zero_names, score, t)
    if score > best_score:
        best_score = score
        print("New best score", score, str(sequence))
    if t > 26:
        return
    last = sequence[-1]
    for nz in non_zero_names:
        d = distances.get_dist(last, nz)
        sequence.append(nz)
        new_non_zero = list(non_zero_names)
        new_non_zero.remove(nz)
        examine(sequence, new_non_zero, score + (25 - t - d ) * valves[nz].flow, t + d + 1)
        sequence.pop()
with open(sys.argv[1]) as f:
    for l in f.read().splitlines():
        v = parse_valve(l)
        valves[v.name] = v
        if v.flow > 0:
            non_zero_valves.append(v)
        for nv in v.next_valves:
            distances.set_dist(v.name, nv, 1)
    calc_all_distances()
    print_distances()

    non_zero_names = ['VR', 'KZ', 'SO', 'SC', 'RO', 'DI', 'OM', 'SP']
    #non_zero_names = ['AJ', 'VG', 'IR', 'JL', 'PW', 'JD', 'RI']

    examine(['AA'], non_zero_names, 0, 0)
    print(best_score)
