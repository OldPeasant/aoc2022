import sys

sys.path.append('../lib')
from pmg import *

from operator import add, mul
from functools import reduce

class Monkey:
    def __init__(self, index, starting_items, operation, test, tgt_monkey_true, tgt_monkey_false):
        self.index = index
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.tgt_monkey_true = tgt_monkey_true
        self.tgt_monkey_false = tgt_monkey_false
        self.inspected_count = 0

class Op:
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def eval(self, val):
        o1 = val if self.arg1 == 'old' else self.arg1
        o2 = val if self.arg2 == 'old' else self.arg2
        ##print("evaluation: ")
        ##print(self.op)
        ##print(self.arg1)
        ##print(self.arg2)
        ##print(val)
        r = self.op(o1, o2)
        ##print(r)
        return r

class DivTest:
    def __init__(self, v):
        self.v = v

    def test(self, d):
        return (d % self.v) == 0

def build_test(line):
    assert(line.startswith("divisible by "))
    v = int(line.split(" by ")[1])
    return DivTest(v)

def build_operation(formula):
    parts = formula.split(" ")
    if parts[1] == '+':
        op = add
    elif parts[1] == '*':
        op = mul
    else:
        raise Exception(parts[1])
    arg0 = (int(parts[0]) if parts[0].isnumeric() else parts[0])
    arg1 = (int(parts[2]) if parts[2].isnumeric() else parts[2])
    ##print("Build Op: " + str(formula) + ": " + str(op) + " / " + str(arg0) + " / " + str(arg1))
    return Op(op, arg0, arg1)
def create_monkey(lines):
    index = int(lines[0].split(' ')[1].split(':')[0])
    starting_items = list( [int(i) for i in lines[1].split(": ")[1].split(",")])
    operation = build_operation(lines[2].split(" new = ")[1])
    test = build_test(lines[3].split(": ")[1])
    assert(lines[4].startswith("    If true: throw to monkey"))
    assert(lines[5].startswith("    If false: throw to monkey"))
    tgt_monkey_true = int(lines[4].split("monkey ")[1])
    tgt_monkey_false = int(lines[5].split("monkey ")[1])
    return Monkey(index, starting_items, operation, test, tgt_monkey_true, tgt_monkey_false)

def process_monkey_turn(index, monkeys):
    curr_m = monkeys[index]
    print("Monkey " + str(curr_m.index))
    for i in curr_m.items:
        curr_m.inspected_count += 1
        print("  inspect " + str(i))
        w = curr_m.operation.eval(i)
        print("    worry level " + str(w))
        b = w // 3
        print("    bored " + str(b))
        t = curr_m.test.test(b)
        print("    Test is " + str(t))
        next_m_id = curr_m.tgt_monkey_true if t else curr_m.tgt_monkey_false
        print("    Throw " + str(b) + " to monkey " + str(next_m_id))
        monkeys[next_m_id].items.append(b)
    curr_m.items = []


with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    grouper = Grouper()
    for l in lines:
        if len(l) == 0:
            continue
        if l.startswith('Monkey'):
            grouper.next()
        grouper.add(l)

    monkeys = {}
    for g in grouper.groups:
        m = create_monkey(g)
        monkeys[m.index] = m

    for turn in range(20):
        for index in sorted(monkeys.keys()):
            print()
            process_monkey_turn(index, monkeys)
        print("After turn " + str(turn + 1))

        for index in sorted(monkeys.keys()):
            print("  Monkey  " + str(index) + ": " + str(monkeys[index].items))
    ic = sorted([m.inspected_count for m in monkeys.values()])
    print(ic)
    print(reduce(mul, ic[-2:]))
