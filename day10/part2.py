import sys

sys.path.append('../lib')
from pmg import *

pixels = []
def check(cycle, x):
    #print("During cycle " + str(cycle) + ", x is " + str(x))
    if abs((cycle % 40) - (x+1)) <= 1:
        pixels.append("#")
    else:
        pixels.append(".")

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
print(len(pixels))
for i in range(0, 240, 40):
    print("".join(pixels[i:i+40]))
