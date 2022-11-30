import sys

if len(sys.argv) <= 1:
    p = "Default"
else:
    p = sys.argv[1]


with open("input1.txt") as f:
    lines = f.read().splitlines()


    for l in lines:
        print(p, l)
