import sys

MOVES = {'U' : (0, 1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}

def move(h, t, direction):
    m = MOVES[direction]
    new_h = (h[0] + m[0], h[1] + m[1])
    if abs(new_h[0] - t[0]) > 1 or abs(new_h[1] - t[1]) > 1:
        new_t = (new_h[0] - m[0], new_h[1] - m[1])
    else:
        new_t = t
    return (new_h, new_t)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    h, t = ( (0, 0), (0, 0) )
    tail_was = {}
    for l in lines:
        direction, amt = l.split(" ")
        for i in range(int(amt)):
            h, t = move(h, t, direction)
            tail_was[str(t[0]) + "-" + str(t[1])] = True
    print(len(tail_was.keys()))
