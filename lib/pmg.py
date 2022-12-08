

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
