import sys


map1 = { 'A' : 'R', 'B' : 'P', 'C' : 'S' }
map2 = { 'X' : 'R', 'Y' : 'P', 'Z' : 'S' }
map_score = {'X' : 0, 'Y' : 3, 'Z' : 6 }
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

def find_mine(him, score):
    for mine in ['R', 'P', 'S']:
        if wins[mine + him] == score:
            return mine
    raise Exception()

with open("input1.txt") as f:
    lines = f.read().splitlines()
    total = 0


    for l in lines:
        h, s = l.split(' ')
        him = map1[h]
        sc = map_score[s]
        me = find_mine(him, sc)
        total += score(him, me)
    print(total)
