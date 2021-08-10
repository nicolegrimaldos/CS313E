# source = where the disks are
# dest = where you want them to land
# spare = the rod you are using to make the transfer

def towers(n, source, spare, dest):
    if n == 1:
        print("Move disk from", source, "to", dest)
    else:
        towers(n - 1, source, dest, spare)
        print("Move disk from", source, "to", dest)
        towers(n - 1, spare, source, dest)


def main():
    towers(3, "A", "B", "C")


main()
