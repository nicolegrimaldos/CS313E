import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


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
    def isLeaf(self, node):
        return node.lchild is None and node.rchild is None

    # Returns an integer representing the sum of the non-leaf nodes
    def get_right_view(self):
        list_leaf = []
        lists_leaf = []
        new = []
        sum = 0
        aNode = self.root
        self.trees_correct(aNode, list_leaf)
        for i in list_leaf:
            sum += i
        # print(list_leaf)
        # self.find()
        # list_leaf.append()
        aNode = self.root
        self.right_tree(aNode, lists_leaf)
        # print(list_leaf)
        aNode = self.root
        self.find_rightmost(aNode, new)
        return new

    def getRLeaf(self, node):
        return node.lchild is None and node.rchild is None

    def right_tree(self, aNode, list_leaf):
        if aNode is not None:
            list_leaf.append(aNode.data)
            self.right_tree(aNode.rchild, list_leaf)

    def find_rightmost(self, aNode, new):
        new.append(aNode.data)
        while not self.getRLeaf(aNode):
            print("here")
            if aNode.rchild:
                aNode = aNode.rchild
                new.append(aNode.data)
            elif aNode.lchild:
                aNode = aNode.lchild
                new.append(aNode.data)

            # print("wow",new)

        if aNode.rchild:
            aNode = aNode.rchild
            new.append(aNode.data)
        elif aNode.lchild:
            aNode = aNode.lchild
            new.append(aNode.data)
        else:
            if aNode.rchild:
                aNode = aNode.rchild
                new.append(aNode.data)
            elif aNode.lchild:
                aNode = aNode.lchild
                new.append(aNode.data)
        print("NEW",new)

    def trees_correct(self, aNode, lists_leaf):
        if aNode != None:
            if self.getRLeaf(aNode):
                lists_leaf.append(aNode.data)
            if aNode != aNode.lchild:
                self.trees_correct(aNode.rchild, lists_leaf)
                self.trees_correct(aNode.lchild, lists_leaf)

    # Returns a list containing the right view of the BST


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

    print(tree.get_right_view())


if __name__ == "__main__":
    main()
