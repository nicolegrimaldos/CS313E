import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # ***There is no reason to change anything above this line***
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def isLeaf(self, node):
         return node.lchild is None and node.rchild is None

    # Returns an integer representing the sum of the non-leaf nodes
    def get_non_leaf_sum(self):
        list_leaf = []
        sum = 0
        aNode = self.root
        self.tree_correct(aNode, list_leaf)
        for i in list_leaf:
            sum += i
        return sum

    def tree_correct(self, aNode, list_leaf):
        if aNode != None:
            if not self.isLeaf(aNode):
                list_leaf.append(aNode.data)
            self.tree_correct(aNode.lchild, list_leaf)
            self.tree_correct(aNode.rchild, list_leaf)




# ***There is no reason to change anything below this line***

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list(map(int, line))  # converts elements into ints

    tree = Tree()
    for i in tree_input:
        tree.insert(i)

    print(tree.get_non_leaf_sum())


if __name__ == "__main__":
    main()
