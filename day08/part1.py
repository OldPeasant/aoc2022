import sys

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]


with open(filename) as f:
    lines = f.read().splitlines()


    for l in lines:
        print(p, l)
