class Tree:
    def __init__(self, name, parent):
        self.parent = parent
        self.children = dict()
        self.name = name
        self.size=0
    def setSize(self, int):
        self.size = self.size+int




f = open("input.txt", "r")

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
    else: tree.setSize(int(xx[0]))
f.close()



def flatten(Tree:Tree):
    output = dict()
    for k, v in Tree.children.items():
        if v.size <=100000 : output[k] = v.size
        if isinstance(v.children, dict):
            output.update(flatten(v))
        else:
            print('fs')
            output[k] = v

    return output

resulting_dict = flatten(root)
sum = 0
for k, v in resulting_dict.items():
    sum = sum + int(v)

print(sum)