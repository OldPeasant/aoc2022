

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

def sig(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        raise Exception()
        
class DictOfLists:
    def __init__(self):
        self.dict = {}
        
    def add(self, key, value):
        self.get(key).append(value)
    
    def get(self, key):
        if key not in self.dict:
            self.dict[key] = []
        return self.dict[key]
        
class DictGrid:
    def __init__(self, value=None):
        self.data = {}
        self.default_value = value
    
    def _key(self, x, y):
    	return str(x) + ":" + str(y)
    	
    def set(self, x, y, v):
        self.data[self._key(x, y)] = v
    def get(self, x, y):
        key = self._key(x, y)
        if key in self.data:
            return self.data[key]
        else:
            return self.default_value
    def all_coords(self):
    	return [ (int(p[0]), int(p[1])) for p in ([k.split(":") for k in self.data.keys()]) ]

class DictGrid3D:
    def __init__(self, value=None):
        self.data = {}
        self.default_value = value
    
    def _key(self, x, y, z):
    	return str(x) + ":" + str(y) + ":" + str(z)
    	
    def set(self, x, y, z, v):
        self.data[self._key(x, y, z)] = v
    def get(self, x, y, z):
        key = self._key(x, y, z)
        if key in self.data:
            return self.data[key]
        else:
            return self.default_value
    def all_coords(self):
    	return [ (int(p[0]), int(p[1]), int(p[2])) for p in ([k.split(":") for k in self.data.keys()]) ]

            
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

def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def points_at_manhattan_dist(p, d):
    result = []
    i = 1
    while i <= d:
        result.append((p[0] - d + i, p[1] + i))
        result.append((p[0] + i, p[1] + d - i))
        result.append((p[0] + d - i, p[1] - i))
        result.append((p[0] - i, p[1] - d + i))
        
        i += 1
    return result
