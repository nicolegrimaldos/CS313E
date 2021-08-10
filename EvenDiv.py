# Input: a is a list of positive integers. 2 < len(a) < 20

# Output: divide the list a into two sub-lists. Get the sum of the two sub-lists. 

# Get the absolute value of the difference between the two sums.

# Return the minimum absolute value difference between the sums of the two sub-lists.
import sys


def sub_sets(a, b, list, idx):
    if idx == len(a):  # no more elements to consider
        list.append(b)
        return
    else:
        c = b[:]  # make a copy of the basket
        b.append(a[idx])  # append the element that you are examining
        sub_sets(a, b, list, idx + 1)
        sub_sets(a, c, list, idx + 1)


def main():
    b = []
    nums = [1,1,1]

    list = []
    sub_sets(nums, b, list, 0)
    print(list)
    min = 1000000
    sum1 = 0
    sum2 = 0
    list.remove(list[0])
    list.remove(list[-1])
    for i in list:
        # print(i)
        for x in list[::-1]:
            # print(x)
            for a in i:
                sum1 += a
            for b in x:
                sum2 += b
            # print("diff",abs(sum1 - sum2))
            if abs(sum1 - sum2) < min:
                min = abs(sum1 - sum2)
                # print("min",min)
            sum1 = 0
            sum2 = 0
    print(nums)


if __name__ == "__main__":
    main()
