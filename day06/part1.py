import sys

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]

with open(filename) as f:
    inp = f.read()
    s = 0
    while True:
        if len(set(inp[s:s+14])) >= 14:
            print(s + 14)
            exit(0)
        s += 1
