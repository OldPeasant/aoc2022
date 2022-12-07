import sys

LIMIT = 100000

if len(sys.argv) <= 1:
    raise Exception("No input file specified")
else:
    filename = sys.argv[1]

class File:
    def __init__(self, parent, size, name):
        self.parent = parent
        self.size = size
        self.name = name

    def print(self, ind):
        print( ("  " * ind) + self.name + " (file, size=" + str(self.size) )
    def get_size(self):
        return self.size

def mysort(d):
    return d.name
class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.contents = []
    def get_child(self, child_name):
        for c in self.contents:
            if c.name == child_name:
                return c
        raise Exception(child_name + " not found in " + self.name)

    def print(self, ind):
            print(("  " * ind) + self.name)
            for c in sorted(self.contents, key=mysort):
                c.print(ind + 1)
    def __str__(self):
        return "Dir[" + self.name + "]"

    def get_size(self):
        s = 0
        for c in self.contents:
            s += c.get_size()
        return s

    def find_smalls(self, arr):
        for c in self.contents:
            if isinstance(c, Dir):
                if c.get_size() <= LIMIT:
                    arr.append(c)
                c.find_smalls(arr)

class Parser:
    def __init__(self):
        self.curr = None
        self.root = Dir(None, "/")

    def cd(self, folder):
        #print("* cd '" + folder + "'")
        if folder == '/':
            self.curr = self.root
        else:
            sub = self.curr.get_child(folder)
            self.curr = sub
    def create_contents(self, cont):
        for c in cont:
            if c.startswith("dir "):
                self.curr.contents.append(Dir(self.curr, c.split("dir ")[1]))
            else:
                size, name = c.split(" ")
                self.curr.contents.append(File(self.curr, int(size), name))

    def process(self, chunk):
        cmd = chunk[0]
        #print("Process cmd " + cmd)
        #print(self.curr)
        if cmd.startswith("$ cd /"):
            self.curr = self.root
        elif cmd.startswith("$ cd .."):
            self.curr = self.curr.parent
        elif cmd.startswith("$ cd "):
            self.cd(cmd.split("$ cd ")[1])
        elif cmd.startswith("$ ls"):
            self.create_contents(chunk[1:])
        else:
            raise Exception(cmd)

    def print(self):
        for f in self.root.contents:
            f.print(0)

with open(filename) as f:
    lines = f.read().splitlines()

    chunks = []
    curr_chunk = []
    for l in lines:
        if l.startswith("$"):
            if len(curr_chunk) > 0:
                chunks.append(curr_chunk)
            curr_chunk = [l]
        else:
            curr_chunk.append(l)
    if len(curr_chunk) > 0:
        chunks.append(curr_chunk)
#    for c in chunks:
#        print("**** chunk ****")
#        for e in c:
#            print("   " + e)
#        print("***********************")
    p = Parser()
    for c in chunks:
        p.process(c)
#    print("-------------------------")
    p.print()
    small_dirs = []
    if p.root.get_size() <= LIMIT:
        small_dirs.append(p.root)
    p.root.find_smalls(small_dirs)
    print("***********************")
    total_smalls = 0
    for sd in small_dirs:
        print(sd, sd.get_size())
        total_smalls += sd.get_size()
    print(total_smalls)
