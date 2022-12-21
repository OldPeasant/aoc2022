import sys

sys.path.append('../lib')
from pmg import *

ORE = 'ore'
CLAY = 'clay'
OBSIDIAN = 'obsidian'
GEODE = 'geode'

EMPTY = {ORE: 0, CLAY: 0, OBSIDIAN: 0, GEODE:0}

def ind(cnt):
    return " " * cnt

def parse_cost_def(cost_def_strings):
    cost_defs = {}
    for cds in cost_def_strings:
        prefix, costs_str = cds.split(' robot costs ')
        material = prefix.split(" ")[1]
        if costs_str.endswith('.'):
            costs_str = costs_str[:-1]
        costs = {}
        for c in costs_str.split('. '):
            for comp in c.split(" and "):
                cost, m = comp.split(' ')
                costs[m] = int(cost)
        cost_defs[material] = costs
    return cost_defs

class Blueprint:
    def __init__(self, input_line):
        top_split = input_line.split(": ") 
        #print("&&&", top_split[0])
        self.b_id = top_split[0].split(' ')[1]
        self.costs = parse_cost_def(top_split[1].split('. '))

    def __repr__(self):
        return "Blueprint %s: %s" % (self.b_id, str(self.costs))
        #for robot_name, costs in self.costs.items():
        #    s += '[' + robot_name + ": " + str(costs) + "]"
        #return s

def possible_geodes(costs, material):
    #print(costs)
    costs_type = costs[GEODE]
    return min( material[OBSIDIAN] // costs_type[OBSIDIAN], material[ORE] // costs_type[ORE] )

def possible_obsidians(costs, material):
    costs_type = costs[OBSIDIAN]
    return min( material[CLAY] // costs_type[CLAY], material[ORE] // costs_type[ORE] )

def possible_clays(costs, material):
    costs_type = costs[CLAY]
    r = material[ORE] // costs_type[ORE]
    #print("having material", material)
    #print("can create clays", r)
    return r

def possible_ores(costs, material):
    costs_type = costs[ORE]
    return material[ORE] // costs_type[ORE]

def do_if_you_can(n):
    if n == 0:
        return [0]
    else:
        return range(n, 0, -1)

all_best = -1

def best_geodes(t, costs, robots, material):
    global all_best
    #print(t, material)
    #print(ind(t) + "Time is %d: %d, %s, %s" % (t, material[GEODE], str(robots), str(material)))
    #if t < 14:
    #    print(t, all_best, material[GEODE])
    if t == 24:
        return material[GEODE]
    if t > 24:
        raise Exception()
    best = material[GEODE]
    for num_create_geodes in do_if_you_can(possible_geodes(costs, material)):
        #print(ind(t), "c ge", num_create_geodes)
        material[OBSIDIAN] -= num_create_geodes * costs[GEODE][OBSIDIAN]
        material[ORE] -= num_create_geodes * costs[GEODE][ORE]
        #print(ind(t), "ores left", material[ORE])
        for num_create_obsidians in do_if_you_can(possible_obsidians(costs, material)):
            #print(ind(t), "c ob", num_create_obsidians)
            material[CLAY] -= num_create_obsidians * costs[OBSIDIAN][CLAY]
            material[ORE] -= num_create_obsidians * costs[OBSIDIAN][ORE]
            #print(ind(t), "ores left", material[ORE])
            for num_create_clays in range(possible_clays(costs, material), -1, -1):
                #print(ind(t), "c cl", num_create_clays)
                material[ORE] -= num_create_clays * costs[CLAY][ORE]
                #print(ind(t), "ores left", material[ORE])
                if num_create_clays == 0:
                    rng_ores = do_if_you_can(possible_ores(costs, material))
                else:
                    rng_ores = range(possible_ores(costs, material), -1, -1)
                for num_create_ores in rng_ores:
                    print(ind(t), "will create", num_create_geodes, "geodes, ", num_create_obsidians, "obsidians, ", num_create_clays, "clays, ", num_create_ores, "ores.")
                    #print(ind(t), "c or", num_create_ores)
                    material[ORE] -= num_create_ores * costs[ORE][ORE]
                    #print(ind(t), "ores left", material[ORE])
                    for m in [ORE, CLAY, OBSIDIAN, GEODE]:
                        assert(material[m] >= 0)
                    print(ind(t), num_create_geodes, num_create_obsidians, num_create_clays, num_create_ores)
                    print(ind(t), "  material ", material)
                    print(ind(t), "robots before", robots)
                    for m in [ORE, CLAY, OBSIDIAN, GEODE]:
                        material[m] += robots[m]
                    print(ind(t), "  material ", material)
                    robots[ORE] += num_create_ores
                    robots[CLAY] += num_create_clays
                    robots[OBSIDIAN] += num_create_obsidians
                    robots[GEODE] += num_create_geodes
                    print(ind(t), "robots after ", robots)
                    b = best_geodes(t + 1, costs, robots, material)
                    if b > best:
                        #print(best)
                        best = b
                    if b > all_best:
                        print(ind(t), "all best", b)
                        all_best = b

                    robots[ORE] -= num_create_ores
                    robots[CLAY] -= num_create_clays
                    robots[OBSIDIAN] -= num_create_obsidians
                    robots[GEODE] -= num_create_geodes

                    for m in [ORE, CLAY, OBSIDIAN, GEODE]:
                        material[m] -= robots[m]

                    material[ORE] += num_create_ores * costs[ORE][ORE]              
                material[ORE] += num_create_clays * costs[CLAY][ORE]
            material[CLAY] += num_create_obsidians * costs[OBSIDIAN][CLAY]
            material[ORE] += num_create_obsidians * costs[OBSIDIAN][ORE]
        material[OBSIDIAN] += num_create_geodes * costs[GEODE][OBSIDIAN]
        material[ORE] += num_create_geodes * costs[GEODE][ORE]
    return best

def analyze_blueprint(b):
    robots = EMPTY.copy()
    robots[ORE] = 1
    material = EMPTY.copy()
    bg = best_geodes(0, b.costs, robots, material)
    print("double check material", material)
    return bg

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    blueprints = []

    for l in lines:
        b = Blueprint(l)
        print(b)
        blueprints.append(b)
    max_quality = -1
    best_blueprint = None
    for b in blueprints[1:]:
        print("analyze blueprint", b.b_id)
        mg = analyze_blueprint(b)

        print("Blueprint %s can produce %d" % (b.b_id, mg))
        quality = mg * int(b.b_id)
        if quality > max_quality:
            max_quality = quality
            best_blueprint = b
    print("best blueprint:", best_blueprint.b_id)
    print("max quality", max_quality)
