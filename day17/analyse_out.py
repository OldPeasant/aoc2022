


with open("out5.txt") as f:
    data = f.read().splitlines()
    ix = 10
    
    for i in range(1500000):
        if (    data[ix  ][:8] == data[i  ][:8] and
                data[ix+1][:8] == data[i+1][:8] and
                data[ix+2][:8] == data[i+2][:8] and
                data[ix+3][:8] == data[i+3][:8] and
                data[ix+4][:8] == data[i+4][:8] and
                data[ix+5][:8] == data[i+5][:8] and
                data[ix+6][:8] == data[i+6][:8] and
                data[ix+7][:8] == data[i+7][:8] and
                data[ix+8][:8] == data[i+8][:8] and
                data[ix+9][:8] == data[i+9][:8] and
                data[ix+10][:8] == data[i+10][:8] and
                data[ix+11][:8] == data[i+11][:8] and
                data[ix+12][:8] == data[i+12][:8] and
                data[ix+13][:8] == data[i+13][:8] and
                data[ix+14][:8] == data[i+14][:8] and
                data[ix+15][:8] == data[i+15][:8]
            ):
            print(i)
            print(data[ix  ][:8], data[i  ][:8])
            print(data[ix+1][:8], data[i+1][:8])
            print(data[ix+2][:8], data[i+2][:8])
            print(data[ix+3][:8], data[i+3][:8])
            print(data[ix+4][:8], data[i+4][:8])
            print(data[ix+5][:8], data[i+5][:8])
            print(data[ix+6][:8], data[i+6][:8])
            print(data[ix+7][:8], data[i+7][:8])
            print(data[ix+8][:8], data[i+8][:8])
