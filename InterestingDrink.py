#  File: InterestingDrink.py

#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of coffee in each store, and a list of integers named money that contains the amount of money
#               Peter will spend in a given day, returns a list of integers representing how many different shops
#               Peter can buy a cup of coffee.

# Student Name: Nicole Grimaldos

# Student UT EID: ng23476

# Course Name: CS 313E

# Unique Number: 52230

import sys


# Input: prices a list of integers containing the price of coffee in each store
#        money  a list of integers containing the amount of money Peter will spend in a given day
# Returns: a list of integers representing how many different shops Peter can buy a cup of coffee.
def find_purchase_options(prices, money):
    list = []
    num = 0
    for i in money:
        for x in prices:
            if int(i) >= int(x):
                num += 1
        list.append(num)
        num = 0
    return list

#######################################################################################################
# No need to change the main()
# The input format the the main is two lines, each line contains some integers split by a single space.
# For example:
# 3 10 8 6 11
# 1 10 3 11
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()
