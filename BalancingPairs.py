#  File: UniqueChars.py

#  Description: Verifying that the string has "balanced" parenthesis
#  and returning the amount of parenthesis needed to become balanced

#  Student Name: Nicole Grimaldos

#  Student UT EID: ng23476

#  Course Name: CS 313E

#  Unique Number: 52235


import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # see the item at the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


def balancingPairs(strng):
    leftStack = Stack()
    rightStack = Stack()
    begStack = Stack()
    tokens = strng
    for item in tokens:
        if item == ")":
            if rightStack.is_empty() and leftStack.is_empty():
                begStack.push(item)
            elif not rightStack.is_empty() and leftStack.is_empty():
                rightStack.push(item)
            else:
                leftStack.pop()
        else:
            if rightStack.is_empty():
                leftStack.push(item)
            else:
                rightStack.pop

    # print(rightStack.stack)
    # print(leftStack.stack)
    # print(begStack.stack)
    return leftStack.size() + rightStack.size() + begStack.size()



# for item in tokens:


def main():
    # read the input String
    f = sys.stdin
    unbalanced = f.readline().strip()
    print(balancingPairs(unbalanced))


if __name__ == "__main__":
    main()