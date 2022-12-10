import sys

sys.path.append('../lib')
from pmg import *

sum_sig = 0
def check(cycle, x):
    global sum_sig
    print("During cycle " + str(cycle) + ", x is " + str(x))
    if (cycle + 20) % 40 == 0:
        strength = cycle * x
        print(strength)
        sum_sig += strength
    else:
        return 0

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    x = 1
    cycle = 0
    for l in lines:
        if l.startswith("noop"):
            cycle += 1
            check(cycle, x)
        elif l.startswith("addx "):
            cycle += 1
            check(cycle, x)
            cycle += 1
            check(cycle,x)
            v = int(l.split(" ")[1])
            x += v
        if cycle > 220:
            break

print(sum_sig)

