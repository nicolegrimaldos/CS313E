#  File: TestBinaryTree.py

#  Description: Find if trees are similar, get the level, height, and number of nodes of a tree

#  Student Name: Nicole Grimaldos

#  Student UT EID: ng23476

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/25/21

#  Date Last Modified: 4/26/21

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

        if self.root is None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while current is not None:
                parent = current
                if data < current.data:
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node

        # search for a node with given data

    def find(self, data):
        current = self.root
        while (current is not None) and (current.data != data):
            if data < current.data:
                current = current.lchild
            else:
                current = current.rchild
        return current

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        current = self.root
        compare = pNode.root
        if current is None and compare is None:
            return True
        if current is None or compare is None:
            return False
        if current.data == compare.data:
            similar = True
        else:
            similar = False
        first = self.evaluate(current)
        second = self.evaluate(compare)
        if first == second and similar is True:
            return True
        else:
            return False

    def operate(self, operand1, operand2, token):
        expr = str(operand1) + str(token) + str(operand2)
        return expr

    def evaluate(self, aNode):
        if aNode is None:
            return 0
        if aNode.lchild is None and aNode.rchild is None:
            return int(aNode.data)
        left = self.evaluate(aNode.lchild)
        right = self.evaluate(aNode.rchild)
        return self.operate(left, right, aNode.data)

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        current = self.root
        lev_list = []
        # if self.root is None:
        #     return lev_list
        # elif level == 0:
        #     lev_list.append(current)
        #     return lev_list
        self.get_level_helper(current, level, lev_list)
        return lev_list

    def get_level_helper(self, aNode, level, lev_list):
        if aNode is None:
            return
        if level == 0:
            lev_list.append(aNode)
        self.get_level_helper(aNode.lchild, level - 1, lev_list)
        self.get_level_helper(aNode.rchild, level - 1, lev_list)

    def add_list(self, lev_list, aNode):
        lev_list.append(aNode)
        print("lev_list",aNode.data)
        return lev_list

    # Returns the height of the tree
    def get_height(self):
        current = self.root
        if self.root is None:
            return 0
        if self.root.lchild is None and self.root.rchild is None:
            return 1
        else:
            return self.compute_heights(current)

    def compute_heights(self, aNode):
        if aNode is None:
            return 0
        else:
            left = (self.compute_heights(aNode.lchild))
            right = (self.compute_heights(aNode.rchild))

        if left > right:
            return left + 1
        else:
            return right + 1

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        current = self.root
        if self.root is None:
            return 0
        return self.find_number(current) - 1

    def find_number(self, aNode):
        if aNode is None:
            return 1
        return self.find_number(aNode.lchild) + self.find_number(aNode.rchild)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints

    tree = Tree()
    for i in tree1_input:
        tree.insert(i)
    # tree.tree_correct(tree.root)

    tree2 = Tree()
    for i in tree2_input:
        tree2.insert(i)
    # tree2.tree_correct(tree2.root)

    tree3 = Tree()
    for i in tree3_input:
        tree3.insert(i)
    # tree3.tree_correct(tree3.root)

    # Test your method is_similar()
    # print(tree.is_similar(tree2))
    # print(tree.is_similar(tree3))

    # Print the various levels of two of the trees that are different
    print(tree.get_level(1))

    # Get the height of the two trees that are different
    # print("get height", tree.get_height())

    # Get the total number of nodes a binary search tree
    print(tree.num_nodes())
    print(tree3.num_nodes())


if __name__ == "__main__":
    main()
