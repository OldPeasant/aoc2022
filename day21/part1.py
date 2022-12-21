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
        return str(monkeys[self.txt))

def cv(expr):
    e = expr.strip()
    if e.isnumeric():
        return NumVal(int(e))
    return SymVal(e)

def parse_expr(expr):
    if '+' in expr:
        return OpAdd(*(cv(v) for v in expr.split(' + ')))
    if '-' in expr:
        return OpSubtr(*(cv(v) for v in expr.split(' - ')))
    if '*' in expr:
        return OpMult(*(cv(v) for v in expr.split(' * ')))
    if '/' in expr:
        return OpDiv(*(cv(v) for v in expr.split(' / ')))
    return cv(expr)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


    for l in lines:
        parts = l.split(": ")
        monkeys[parts[0]] = parse_expr(parts[1])
    r = monkeys['root']
    print(r.a)
    print("must be equal to")
    print(r.b)

