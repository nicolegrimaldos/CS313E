#  File: CounterRotate.py

#  Description: Rotates a linked list to the left (counter-clockwise) rot_amt places t times 

#  Student Name: Nicole Grimaldos

#  Student UT EID: ng23476

#  Course Name: CS 313E

#  Unique Number: 

import sys

class Link (object):
    # do not change this constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # create a linked list -- do not change this constructor
    def __init__(self):
        self.first = None

    # helper function to add an item at the end of a list
    # you can use this if you want, but do not delete it
    def insert_last (self, data): 
        newLink = Link(data)
        current = self.first

        if current == None:
            self.first = newLink
            return

        while current.next != None:
            current = current.next

        current.next = newLink

    # helper function to copy the contents of the current linked list
    # returns new linked list
    # you can use this if you want, but do not delete it
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list

    # helper function to count number of links
    # returns number of links
    # you can use this if you want, but do not delete it
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    # string representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res

    def find(self, data):
        current = self.first
        if current is None:
            return None
        while current.data != data:
            current = current.next

        return current

    # COMPLETE THIS FUNCTION
    # return a new linked list that results from the rotation
    # do not change this linked list
    def rotate(self, rot_amt, t):
        newLink = self.copy_list()
        if newLink.first.next is None:
            return newLink
        for i in range(rot_amt):
            for i in range(t):
                current = newLink.first
                find_last = newLink.first
                while find_last.next is not None:
                    find_last = find_last.next
                last = find_last
                prev = current
                current = current.next
                last.next = prev
                prev.next = None
                newLink.first = current


            #
            # for i in range(t):
            #     last.next = current
            #     print("ln",last.next.data)
            #     print("last dat",last.data)
            #     last = current.next
            #     current = current.next
            # last.next = None
        return newLink


        
# DO NOT CHANGE MAIN
def main():
    ll = LinkedList()
    
    data = list(map(int, input().split()))

    # populate linked list with data
    for d in data:
        ll.insert_last(d)

    rot_amt, t = list(map(int, input().split()))

    rotated = ll.rotate(rot_amt, t)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)

if __name__ == "__main__":
    main()