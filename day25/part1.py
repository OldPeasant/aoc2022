import sys

sys.path.append('../lib')
from pmg import *

def snafu_digit_to_dec(c):
    if c == '=':
        return -2
    elif c == '-':
        return -1
    else:
        return int(c)

def snafu_to_dec(txt):
    v = 1
    s = 0
    for c in reversed(txt):
        cv = snafu_digit_to_dec(c)
        s += v * cv
        v *= 5
    return s

def dec_to_snafu(d):
    if d == 0:
        return ''
    m5 = d % 5
    if m5 == 4:
        l = '-'
        d += 5 - 1
    elif m5 == 3:
        l = '='
        d += 5 - 2
    else:
        l = str(m5)
    return dec_to_snafu(d // 5) + l

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


    s = 0
    for l in lines:
        d = snafu_to_dec(l)
        back = dec_to_snafu(d)
        print(l, d, back)
        s += d
    print(dec_to_snafu(s))
