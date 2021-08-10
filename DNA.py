#  File: DNA.py

#  Description:

#  Student Name:Camila Bohorquez

#  Student UT EID: cb48598

#  Partner Name: Nicole Grimaldos

#  Partner UT EID: ng23476

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 1/21/2021

#  Date Last Modified: 1/22/2021

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.


####### ASSIGNMENT URL: https://www.cs.utexas.edu/users/mitra/csSpring2021/cs313/assgn/assgn0.html
####### LIST FUNCTIONS URL: https://www.programiz.com/python-programming/methods/list/sort

def longest_subsequence(s1, s2):
    common_substring_list = []
    longest_subs = []

    # find the longest string and shortest
    if s2 > s1:
        longest = s2
        shortest = s1
    else:
        longest = s1
        shortest = s2

    m = 0
    # for each letter in the shortest string
    for letter in shortest:
        # find the length
        n = len(shortest)

        while n != 2 and m != n:
            # create a temp sequence
            temp = shortest[m:n]
            # see if temp sequence is in the longest string
            # also verify that temp sequence is more than 2
            if str(temp) in longest and len(temp) > 2:
                # append the found sequence in a list
                common_substring_list.append(temp)
            n -= 1
        m += 1
    # empty common list return "No Common Subsequence Found"
    if len(common_substring_list) == 0:
        print("No Common Subsequence Found")


    # elif to complete the work if there is a common subsequence
    else:
    # find the longest length subset
        max_length = len(max(common_substring_list, key=len))
        # go through the list and find the longest substrings
        for x in common_substring_list:
            # make sure the length is longer than three
            # and is larger or equal to the maximum length substring
            if len(x) >= 3 and len(x) >= max_length:
                longest_subs.append(x)
                max_length = len(x)
        #  sort the list of the longest substrings
        longest_subs.sort()
        # print in alphabetical order
        for item in longest_subs:
            print(item)


def main():
    # read the data
    file1 = open("dna.in", "r")

    numPairs = int(file1.readline())
    # for each pair
    for num in range(numPairs):
        s1 = file1.readline()

        s2 = file1.readline()
        longest_subsequence(s1, s2)
        print()

    # results printed by longest_sub


if __name__ == "__main__":
    main()