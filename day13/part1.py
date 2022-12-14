import sys

sys.path.append('../lib')
from pmg import *

class PIter:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def peek(self):
        if self.pos >= len(self.data):
            return None
        return self.data[self.pos]
     
    def next(self):
        if self.pos >= len(self.data):
            return None
        c = self.data[self.pos]
        self.pos += 1
        return c

def tokenize(line):
    tokens = []
    n = ''
    for c in line:
        if c in ['[', ']', ',']:
            if len(n) > 0:
                tokens.append(int(n))
                n = ''
            tokens.append(c)
        else:
            n += c
    if len(n) > 0:
        tokens.append(int(n))
    return tokens

def build_list(piter):
    assert(piter.next() == '[')
    result = []
    while True:
        p = piter.peek()
        if p == ',':
            piter.next()
        elif type(p) == int:
            result.append(piter.next())
        elif p == ']':
            piter.next()
            return result
        elif p == '[':
            result.append(build_list(piter))
        else:
            raise Exception()

def build(piter):
    n = piter.peek()
    if n == '[':
        return build_list(piter)
    else:
        raise Exception()

def parse(line):
    tokens = tokenize(line)
    piter = PIter(tokens)
    return build(piter)

def right_order_lists(left, right):
    print(" check lists " + str(left) + " vs " + str(right))
    index = 1
    for l, r in zip(left, right):
        print("elements " + str(index) + " of lists:" + str(l) + " vs " + str(r))
        if l is None:
            print("no more elements on the left => true")
            return True
        if r is None:
            print("no more elements on thr right => false")
            return False

        c = right_order((l, r))
        if c is not None:
            print("so comparing lists gives us " + str(c))
            return c
        index += 1
    if len(left) > len(right):
        return False
    if len(left) < len(right):
        return True
    print("can't decide")
    return None

def right_order(pair):
    left, right = pair
    if type(left) == int and type(right) == int:
        print("both integers", left, right)
        if left < right:
            print("left < right => True")
            return True
        elif left > right:
            print("left > right => False")
            return False
        else:
            print(" left == right => don't know")
            return None
    if type(left) == list and type(right) == list:
        print(" two lists => check lists right order")
        c = right_order_lists(left, right)
        if c is not None:
            return c
    if type(left) == int and type(right) == list:
        print("left int, right list => check right order list")
        c = right_order_lists([left], right)
        if c is not None:
            return c
    if type(left) == list and type(right) == int:
        print("left is list, right is int => check right order list")
        c = right_order_lists(left, [right])
        if c is not None:
            return c
    print("don't know")
    return None

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    pairs = []

    index = 0
    while True:
        line1 = parse(lines[index])
        line2 = parse(lines[index + 1])
        pairs.append( (line1, line2) )
        #assert(index >= len(len(lines) + 1) or len(lines[index + 2]) == 0)
        index += 3
        if index >= len(lines):
            break

    sum_ix = 0
    index = 1
    for p in pairs:
        print("======= Checking pair " + str(index) + ": "  + str(p[0]) + " vs " + str(p[1]))
        if right_order(p):
            print("  right order, sum += " + str(index))
            sum_ix += index
        else:
            print("  wrong order")
        index += 1
    print(sum_ix)
