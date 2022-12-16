import sys

sys.path.append('../lib')
from pmg import *

valves = {}

class Valve:
    def __init__(self, name, flow, next_valves):
        self.name = name
        self.flow = flow
        self.next_valves = next_valves
        self.is_open = False

    def possible_actions(self):
        actions = []
        if not self.is_open and self.flow > 0:
            actions.append(['open'])
        for n in self.next_valves:
            actions.append(['move', n])
        return actions

    def __repr__(self):
        return "Valve[%s, %d, %s]" % (self.name, self.flow, "/".join(v for v in self.next_valves))

def parse_valve(line):
    by_space = line.split(' ')
    name = by_space[1]
    flow = int(by_space[4].split('=')[1].split(';')[0])
    #print(line)
    if "to valves " in line:
        next_valves = line.split("to valves ")[1].split(", ")
    elif "to valve " in line:
        next_valves = line.split("to valve ")[1].split(", ")
    else:
        raise Exception()
    return Valve(name, flow, next_valves)


with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    for l in lines:
        v = parse_valve(l)
        valves[v.name] = v
    with open(sys.argv[1] + ".dot", 'w') as fout:
        fout.write("digraph {\n")
        for src_name in valves.keys():
            src = valves[src_name]
            fout.write("    %s [label=\"%s [%s]\"]\n" % (src_name, src_name, str(src.flow)))
        for src_name in valves.keys():
            src = valves[src_name]
            for tgt in valves[src_name].next_valves:
                if src_name < tgt:
                    print(src_name, tgt)
                    fout.write("    %s -> %s\n" % (src_name, tgt))
        fout.write("}")
