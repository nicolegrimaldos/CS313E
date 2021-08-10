import sys


def binary_search(a):
    if a < 0:
        a = abs(a)
        neg = True
    else:
        neg = False
    lo = 0
    hi = abs(a)
    error = 0.000001
    while lo <= hi:
        mid = (lo + hi) / 2
        if mid ** 3 > a:
            hi = mid
        elif abs((mid ** 3) - a) < error:
            if neg:
                return mid * -1
            return mid
        else:
            lo = mid

    return -1


line = sys.stdin.readline()
print(binary_search(int(line)))
