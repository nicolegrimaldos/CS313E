def sub_sets(a, b, idx):
    if idx == len(a):  # no more elements to consider
        print(b)
        return
    else:
        c = b[:]  # make a copy of the basket
        b.append(a[idx])  # append the element that you are examining
        sub_sets(a, b, idx + 1)
        sub_sets(a, c, idx + 1)


def main():
    a = ("A", "B", "C", 'D',)
    b = []
    sub_sets(a, b, 0)


main()
