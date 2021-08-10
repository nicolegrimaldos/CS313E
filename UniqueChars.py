#  File: UniqueChars.py

#  Description: Finding a list of strings that are the correct length and comprised of letters in a given alphabet

#  Student Name: Nicole Grimaldos

#  Student UT EID: ng23476

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 4/2/21

#  Date Last Modified: 4/2/21

import sys


# Input:  alphabet is a list of characters that you will
#         build your strings from.
#         n is an integer and is the length of the unique-character strings
#         that you will need to construct.
# Output: return a list of strings that are length n, are comprised only of
#         characters from alphabet, and have unique characters.
# def sub_sets(a, b, list, idx):
#   if idx == len(a):  # no more elements to consider
#     list.append(b)
#     return
#   else:
#     c = b[:]  # make a copy of the basket
#     b.append(a[idx])  # append the element that you are examining
#     sub_sets(a, b, list, idx + 1)
#     sub_sets(a, c, list, idx + 1)


def unique(n, alphabet):
    '''Ex. unique(2, ['a', 'b', 'c']) -> ['ab', 'ac', 'ba', 'bc', 'ca', 'cb]'''

    list = []

    for i in alphabet:
        char = str(i)
        # print("char",char)
        for x in alphabet:
            # print("x",x)

            if len(char)+1 > n:
                char = str(i)
            if len(char) < n:
                char += str(x)
                # print("added",char)
            if char not in list and (i+i) not in char and len(char) == n:
                # print("now in list", char)
                list.append(char)

    return list


# ***There is no reason to change anything below this line***

def main():
    alphabet = sys.stdin.readline().split()
    n = int(sys.stdin.readline())

    result = unique(n, alphabet)
    result.sort()
    for r in result:
        print(r)


if __name__ == "__main__":
    main()
