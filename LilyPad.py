#  File: LilyPad.py

#  Description: Determines the distinct amount of ways Foo can get to the other side
#               of a pond with n lily pads by hopping either 1 or 2 lily pads at a time

#  Student Name: Nicole Grimaldos

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 52230

import sys


# Input: n is an int of how many lily pads there are
# Output: return an integer of how many distinct ways there are to cross the pond (order matters)
def routes_memo(n, memo):
    if n == 0 or n == 1:
        return memo[n]
    else:
        if n >= len(memo):
            # value is not in memo then compute it and store it
            f = routes_memo(n - 1, memo) + routes_memo(n - 2, memo)
            memo.append(f)
            return f
        else:
            return memo[n]


def distinct_ways(n):
    memo = [0, 1]
    sum = 1
    for i in range(n):
        routes_memo(i, memo)
    # print(len(memo))
    if len(memo) == 2:
        memo.remove(memo[1])
    for i in memo:
        sum += i
    # print(sum)
    return sum


def main():
    # read number of lily pads
    n = int(input())

    # get the result from your call to distinct_ways()
    result = distinct_ways(n)

    # print the result to standard output
    print(result)


if __name__ == "__main__":
    main()
