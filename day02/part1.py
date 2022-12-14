import sys


map1 = { 'A' : 'R', 'B' : 'P', 'C' : 'S' }
map2 = { 'X' : 'R', 'Y' : 'P', 'Z' : 'S' }

wins = {
        'RR' : 3,
        'RP' : 0,
        'RS' : 6,
        'PR' : 6,
        'PP' : 3,
        'PS' : 0,
        'SR' : 0,
        'SP' : 6,
        'SS' : 3
}
shapeval = {'R' : 1, 'P' : 2, 'S' : 3 }
def score(h1, h2):
    return shapeval[h2] + wins[h2 + h1]


with open("input1.txt") as f:
    lines = f.read().splitlines()
    total = 0


    for l in lines:
        h, m = l.split(' ')
        him = map1[h]
        me = map2[m]
        total += score(him, me)
    print(total)
