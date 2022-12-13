import sys

sys.path.append('../lib')
from pmg import *

from functools import cmp_to_key

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

def compare_pairs(p1, p2):
    c = right_order((p1, p2))
    if c is True:
        return -1
    elif c is False:
        return 1
    elif c is None:
        return 0
    else:
        raise Exception()

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    items = list([parse(l) for l in lines if len(l) > 0])
    div1 = [[2]]
    div2 = [[6]]
    items.append(div1)
    items.append(div2)

    print('----------------------------------------------------')
    for s in items:
        print(s)

    st = sorted(items, key=cmp_to_key(compare_pairs))

    print("====================================================")
    for s in st:
        print(s)
    index = 1
    for s in st:
        if s == div1:
            ix_div1 = index
        if s == div2:
            ix_div2 = index
        index += 1

    print(ix_div1)
    print(ix_div2)
    print(ix_div1 * ix_div2)
