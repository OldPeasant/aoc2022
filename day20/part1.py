import sys

sys.path.append('../lib')
from pmg import *

class MyNum:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return "N(%d)" % self.n

def swap(numbers, ix1, ix2):
    numbers[ix1], numbers[ix2] = numbers[ix2], numbers[ix1]

def move_pos(numbers, ix, n):
    #print("moving pos", numbers, ix, n)
    for i in range(n):
        if ix == len(numbers) - 1:
            nn = [numbers[0]]
            nn.append(numbers[-1])
            nn.extend(numbers[1:-1])
            numbers = nn
            ix = 1
        else:
            swap(numbers, ix, ix + 1)
            ix += 1
            if ix == len(numbers):
                ix = 0
        #print("    ", numbers)
    #print("moving pos done", numbers)

    return numbers

def move_neg(numbers, ix, n):
    #print("moving neg", numbers, ix, n)
    for i in range(abs(n)):
        if ix == 0:
            nn = numbers[1:-1]
            nn.append(numbers[0])
            nn.append(numbers[-1])
            numbers = nn
            ix = len(numbers) - 2
        else:
            swap(numbers, ix, ix - 1)
            ix -= 1
            if ix < 0:
                ix = len(numbers) - 1

        #print("  ix  ", numbers)

    #print("moving neg done", numbers)
    return numbers

def move(numbers, n):
    l = len(numbers)
    ix = numbers.index(n)
    #print("index of", n, "is", ix)
    if n.n > 0:
        return move_pos(numbers, ix, n.n)
    if n.n < 0:
        return move_neg(numbers, ix, n.n)
    if n.n == 0:
        return numbers
    raise Exception()

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    orig_numbers = list(MyNum(int(l)) for l in lines)
    
    s = set(orig_numbers)
    s.update(orig_numbers)
    assert(len(orig_numbers) == len(s))

    work_numbers = list(orig_numbers)

    for n in orig_numbers:
        #print()
        #print("moving", n)
        work_numbers = move(work_numbers, n)
        #print(work_numbers)
    #print("==================================")
    #print(work_numbers)
    index_of_0 = -1
    for i, n in enumerate(work_numbers):
        if n.n == 0:
            index_of_0 = i
    if index_of_0 < 0:
        raise Exception()

    v1 = work_numbers[ (index_of_0 + 1000) % len(work_numbers)]
    v2 = work_numbers[ (index_of_0 + 2000) % len(work_numbers)]
    v3 = work_numbers[ (index_of_0 + 3000) % len(work_numbers)]

    print(v1, v2, v3)
    print(v1.n + v2.n + v3.n)

