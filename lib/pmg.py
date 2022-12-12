

class Grouper:
    def __init__(self):
        self.groups = []
        self.new_on_next = True

    def add(self, item):
        if self.new_on_next:
            self.groups.append([])
            self.new_on_next = False
        self.groups[-1].append(item)

    def next(self):
        self.new_on_next = True

def multi_list(*args, value=None):
    if len(args) > 1:
        return [ multi_list(*list(args)[1:], value=value) for x in range(args[0])]
    else:
        return [value for x in range(args[0])]

class Grid:
    def __init__(self, width, height, value=None):
        self.data = multi_list(width, height, value=value)

    def set(self, x, y, v):
        self.data[x][y] = v

    def get(self, x, y):
        return self.data[x][y]

    def set_t(self, coord, v):
        self.set(coord[0], coord[1], v)

    def get_t(self, coord):
        return self.get(coord[0], coord[1])

    def find_one(self, value):
        for x, row in enumerate(self.data):
            for y, v in enumerate(row):
                if value == v:
                    return (x, y)

    def find_all(self, value):
        matches = []
        for x, row in enumerate(self.data):
            for y, v in enumerate(row):
                if value == v:
                    matches.append( (x, y) )
        return matches

    def is_inside_t(self, pt):
        x, y = pt
        if x >= 0 and x < len(self.data):
            if y >= 0 and y < len(self.data[x]):
                return True
        return False
