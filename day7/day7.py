class Tree:
    def __init__(self, name, parent):
        self.parent = parent
        self.children = dict()
        self.name = name
        self.files = dict()
        self.size=0
    def setSize(self, int):
        self.size = self.size+int

f = open("/home/markussigurbjornsson/Documents/adventOfCode2022/day7/input.txt", "r")

root = Tree("/", None)
tree = root
for x in f:
    xx = x.split()
    if xx[0] == "$":
        if xx[1] == "cd":
            if xx[2] == "/": tree = root
            elif xx[2] == "..": tree = tree.parent
            else: tree = tree.children[xx[2]]
    elif xx[0] == "dir": tree.children[xx[1]] = (Tree(xx[1], tree))
    else: tree.files[xx[1]] = int(xx[0])
f.close()

def set_size(Tree:Tree):
    size = 0
    for k, v in Tree.children.items():
        if isinstance(v.children, dict):
            size = size + set_size(v)
        else:
            pass
    for l, n in Tree.files.items():
        size = size + int(n)
    Tree.size=size
    return size

def flatten(Tree:Tree):
    d = dict()
    for k, v in Tree.children.items():
        if tree.size <= 100000: print(Tree.size)
        if isinstance(v.children, dict):
            d.update(flatten(v))
    return d 


print(root.size)
c = set_size(root)
print(root.size)
flatten(root)