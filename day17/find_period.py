
def check_period(data, p):
    print("check period", p)
    for i in range(1, 5000):
        print(data[i*p][1] - data[(i+1) * p][1])

with open('out2.txt') as f:
    data = []
    for l in f.read().splitlines():
        parts = l.split(' ')
        data.append( (int(parts[0]), int(parts[1])) )

    #for p in range(1, 1000000):
    #    check_period(data, p)
    check_period(data, 2120)
