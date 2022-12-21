
with open('base0.txt') as f:
    last = 0
    for l in f.read().splitlines():
        curr = int(l)
        print(curr - last)
        last = curr
