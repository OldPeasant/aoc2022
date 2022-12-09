import sys

MOVES = {'U' : (0, 1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}

def pull(h, t):
    ad0, ad1 = ( abs(h[0] - t[0]), abs(h[1] - t[1]))
    if ad0 <= 1 and ad1 <= 1:
        return t
    if ad0 > 1 and ad1 > 1:
        return ( (h[0] + t[0]) // 2, (h[1] + t[1]) // 2)
    elif ad0 > 1:
        return (h[0] - (h[0] - t[0]) // 2, h[1])
    elif ad1 > 1:
        return (h[0], h[1] - (h[1] - t[1]) // 2)
    else:
        raise Exception()

def move_snake(s, direction):
    m = MOVES[direction]
    new_snake = [ (s[0][0] + m[0], s[0][1] + m[1]) ]
    for t in snake[1:]:
        new_snake.append(pull(new_snake[-1], t))
    return new_snake

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    snake = list( ((0, 0) for i in range(10) ))
    tail_was = {}
    for l in lines:
        direction, amt = l.split(" ")
        for i in range(int(amt)):
            snake = move_snake(snake, direction)
            t = snake[-1]
            tail_was[str(t[0]) + "-" + str(t[1])] = True
    print(len(tail_was.keys()))
