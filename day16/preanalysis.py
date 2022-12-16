from itertools import chain, combinations

all_nz = ['VR', 'KZ', 'AJ', 'VG', 'IR', 'SO', 'SC', 'RO', 'JL', 'PW', 'DI', 'JD', 'SP', 'OM', 'RI']
right = ['VR', 'RO', 'SP', 'KZ', 'DI', 'SO', 'SC']

def is_good(mine):
    elefants = list( o for o in all_nz if o not in mine)
    print("check is good")
    print(" ", mine)
    print(" ", elefants)

    for m in mine:
        if m not in right:
            print(" ", "no good")
            return False
    for e in elefants:
        if e in right:
            print(" ", "no good")
            return False
    print(" ", "yes good")
    return True


count = 0
s = all_nz
for p in chain.from_iterable(combinations(s, r) for r in range(len(s)+1)):
    if is_good(p):
        count += 1
print(count)
