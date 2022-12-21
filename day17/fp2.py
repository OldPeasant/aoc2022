def find_p(data, p):
    print("check period %d" % p)
    i = 1000000
    while True:
        if data[p+i] != data[2*p+i]:
            print("                It's not period %d (%d)" % (p, i))
            return
        i += 1

def validate_period(heights, st, p):
    i = st
    num = 0
    while i + st < len(heights):
        print("check %d / %d" % (i, i + p))
        if heights[i+p] - heights[i] != 2667:
            print(" no, wrong at number %d" % num)
            return
        print("  yes")
        num += 1
        i += 1
with open('heights_real.txt') as f:
    heights = []
    for l in f.read().splitlines():
        heights.append(int(l))
    
    p = 1735
    st = 1038142
    #validate_period(heights, st, p)
    #exit(0)
    h0 = heights[st]
    tgt = 1000000000000

    rema = tgt - st
    print("rema", rema)
    times = rema // p
    print("times", times)
    upper = tgt - ((times * p) + st)
    print("upper", upper)
    total = h0 + times * 2667
    print("total incompl", total)
    i_start = st + times * p + 1
    i_end = tgt
    print("start end", i_start, i_end)
    print("len loop", i_end - i_start)
    num = 0
    for i in range(i_start, i_end):
        total += heights[st + num - 1]
        num += 1
        print(num)
    print(total)
    exit(0)
    i = st
    while i < len(heights):
        print(heights[i] - heights[i - p])
        i +=1
