import sys

sys.path.append('../lib')
from pmg import *

monkeys = {}

class OpAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def evaluate(self):
        return self.a.evaluate() + self.b.evaluate()

    def __repr__(self):
        return str(self.a) + '+' + str(self.b)

class OpSubtr:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def evaluate(self):
        return self.a.evaluate() - self.b.evaluate()

    def __repr__(self):
        return str(self.a) + '-' + str(self.b)

class OpMult:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def evaluate(self):
        return self.a.evaluate() * self.b.evaluate()

    def __repr__(self):
        return str(self.a) + '*' + str(self.b)

class OpDiv:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def evaluate(self):
        return self.a.evaluate() / self.b.evaluate()

    def __repr__(self):
        return str(self.a) + '/' + str(self.b)

OPERATIONS = {'+' : OpAdd, '-' : OpSubtr, '*' : OpMult, '/' : OpDiv}

class NumVal:
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        return self.v

    def __repr__(self):
        return str(self.v)

class SymVal:
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self):
        return monkeys[self.txt].evaluate()

    def __repr__(self):
        return str(monkeys[self.txt])

def parse(expr):
    e = expr.strip()
    if e.isnumeric():
        return NumVal(int(e))
    return SymVal(e)

with open(sys.argv[1]) as f:
    for l in f.read().splitlines():
        name, value = l.split(": ")
        value_parts = value.split(' ')
        if len(value_parts) == 1:
            monkeys[name] = parse(value_parts[0])
        else:
            monkeys[name] = OPERATIONS[value_parts[1]](parse(value_parts[0]), parse(value_parts[2])  )
    print(monkeys['root'].evaluate())

