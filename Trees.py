class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
#       self.parent = None
#       self.visited = False

class Tree(object):
    def __init__(self):
        self.root = None

    def