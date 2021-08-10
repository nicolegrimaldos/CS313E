import sys

'''
Input:  coins is a dictionary representing how many of each type of coin you have (value -> amount)
        amount is the target amount you want to make change for
Output: True if it possible to make exact change using the coins provided, False otherwise
'''


def sub_sets(a, b, list, idx):
    if idx == len(a):  # no more elements to consider
        list.append(b)
        return
    else:
        c = b[:]  # make a copy of the basket
        b.append(a[idx])  # append the element that you are examining
        sub_sets(a, b, list, idx + 1)
        sub_sets(a, c, list, idx + 1)


def canMakeChange(coins, amount):
    b = []
    list = []
    sets = []
    sum = 0
    sums = []
    for i in coins:
        for x in range(coins[i]):
            sets.append(i)
    sub_sets(sets, b, list, 0)
    for a in list:
        for b in a:
            sum += b
        sums.append(sum)
        sum = 0

    if amount in sums:
        return True
    else:
        return False


def main():
    f = sys.stdin
    num_coins, amount = [int(x.strip()) for x in f.readline().split()]
    coins = {}
    for _ in range(num_coins):
        coin_val, coin_amt = [int(x.strip()) for x in f.readline().split()]
        coins[coin_val] = coin_amt
    print(canMakeChange(coins, amount))


if __name__ == "__main__":
    main()
