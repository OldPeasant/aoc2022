import sys

sys.path.append('../lib')
from pmg import *

monkeys = {}

class Op:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def contains_unknown(self):
#        print("check contains unknown")
#        print(self.a, self.a.contains_unknown())
#        print(self.b, self.b.contains_unknown())
        any_of_them = self.a.contains_unknown() or self.b.contains_unknown()
#        print("any of them", self.a, self.b, any_of_them)
        return any_of_them

    def resolve_unknown(self, other_expr):
        if self.a.contains_unknown():
            return self.resolve_unknown_left(other_expr)
        elif self.b.contains_unknown():
            return self.resolve_unknown_right(other_expr)

class OpAdd(Op):
    def __init__(self, a, b):
        super().__init__(a, b)

    def evaluate(self):
        return self.a.evaluate() + self.b.evaluate()

    def __repr__(self):
        return '(' + str(self.a) + '+' + str(self.b) + ')'

    def resolve_unknown_left(self, other_expr):
        return Equation(self.a, OpSubtr(other_expr, self.b))

    def resolve_unknown_right(self, other_expr):
        return Equation(self.b, OpSubtr(other_expr, self.a))
        
class OpSubtr(Op):
    def __init__(self, a, b):
        super().__init__(a, b)

    def evaluate(self):
        return self.a.evaluate() - self.b.evaluate()

    def __repr__(self):
        return '(' + str(self.a) + '-' + str(self.b) + ')'

    def resolve_unknown_left(self, other_expr):
        return Equation(self.a, OpAdd(other_expr, self.b))

    def resolve_unknown_right(self, other_expr):
        return Equation(self.b, OpSubtr(self.a, other_expr))

class OpMulti(Op):
    def __init__(self, a, b):
        super().__init__(a, b)

    def evaluate(self):
        return self.a.evaluate() * self.b.evaluate()

    def __repr__(self):
        return '(' + str(self.a) + '*' + str(self.b) + ')'

    def resolve_unknown_left(self, other_expr):
        return Equation(self.a, OpDiv(other_expr, self.b))

    def resolve_unknown_right(self, other_expr):
        return Equation(self.b, OpDiv(other_expr, self.a))

class OpDiv(Op):
    def __init__(self, a, b):
        super().__init__(a, b)

    def evaluate(self):
        return self.a.evaluate() / self.b.evaluate()

    def __repr__(self):
        return '(' + str(self.a) + '/' + str(self.b) + ')'

    def resolve_unknown_left(self, other_expr):
        return Equation(self.a, OpMulti(other_expr, self.b))

    def resolve_unknown_right(self, other_expr):
        return Equation(self.b, OpDiv(self.a, other_expr))

class NumVal:
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        return self.v

    def __repr__(self):
        return str(self.v)

    def contains_unknown(self):
        return False

class SymVal:
    def __init__(self, txt):
        #print("CREATE SYMVAL:", txt)
        self.txt = txt

    def evaluate(self):
        return monkeys[self.txt].evaluate()

    def __repr__(self):
        return '(' + str(monkeys[self.txt]) + ')'

    def contains_unknown(self):
        return monkeys[self.txt].contains_unknown()

class Unknown:
    def __init__(self):
        pass
    def evaluate(self):
        raise Exception("Can't evaluate the unknown")

    def __repr__(self):
        return "x"

    def contains_unknown(self):
        return True

def resolve_left(expr_to_resolve, expr_to_eval):
    if isinstance(expr_to_resolve, Unknown):
        return expr_to_eval
    if isinstance(expr_to_resolve, Op):
        return expr_to_resolve.resolve_unknown(expr_to_eval)
    if isinstance(expr_to_resolve, SymVal):
        v = monkeys[expr_to_resolve.txt]
        return resolve_left(v, expr_to_eval)
    else:
        raise(Exception(str(expr_to_resolve) + " / " + str(expr_to_resolve.__class__)))

class Equation:
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def resolve(self):
        #print("Resolve equation:")
        #print(self.expr1)
        #print(self.expr2)
        if isinstance(self.expr1, Unknown):
            return self.expr2.evaluate()
        if isinstance(self.expr2, Unknown):
            return self.expr1.evaluate()
        if self.expr1.contains_unknown():
            new_eq = resolve_left(self.expr1, self.expr2)
        elif self.expr2.contains_unknown():
            new_eq = resolve_left(self.expr2, self.expr1)
        else:
            print("resolve equations fails")
            print(self.expr1)
            print(self.expr1.__class__)
            print(self.expr1.txt)
            print(self.expr2)
            print(self.expr2.__class__)
            print(self.expr2.txt)
            raise Exception()
        return new_eq.resolve()
def cv(expr):
    e = expr.strip()
    if e.isnumeric():
        return NumVal(int(e))
    if e == 'humn':
        return Unknown()
    else:
        return SymVal(e)

def parse_expr(expr):
    if '+' in expr:
        return OpAdd(*(cv(v) for v in expr.split(' + ')))
    if '-' in expr:
        return OpSubtr(*(cv(v) for v in expr.split(' - ')))
    if '*' in expr:
        return OpMulti(*(cv(v) for v in expr.split(' * ')))
    if '/' in expr:
        return OpDiv(*(cv(v) for v in expr.split(' / ')))
    return cv(expr)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


    for l in lines:
        parts = l.split(": ")
        monkeys[parts[0]] = parse_expr(parts[1])
    r = monkeys['root']
    eq = Equation(r.a, r.b)
    print(eq.resolve())
    
