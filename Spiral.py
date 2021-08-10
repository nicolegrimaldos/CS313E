def createSpiral(n):
    # find number of rows
    num = n
    # create empty list
    list = [[0 for i in range(num)] for j in range(num)]

    # reference key for the middle one
    middleKey = (n // 2)
    list[middleKey][middleKey] = 1


    # initial number 2
    number = 2
    xKey = middleKey
    yKey = middleKey + 1


    downBy = 1
    leftBy = 2
    upBy = 2
    rightBy = 2
    list[xKey][yKey] = number
    print(list)
    number += 1
    maxNumber = num ** 2 + 1

    while number != maxNumber:
        #input numbers going down
        for i in range(downBy):
            xKey += 1
            list[xKey][yKey] = number
            number += 1

        for i in range(leftBy):
            yKey -= 1
            list[xKey][yKey] = number
            number += 1

        for i in range(upBy):
            xKey -= 1
            list[xKey][yKey] = number
            number += 1

        for i in range(rightBy):
            yKey += 1
            list[xKey][yKey] = number
            number += 1

        yKey += 1
        list[xKey][yKey] = number
        number += 1

        downBy += 2
        leftBy += 2
        upBy += 2
        rightBy += 2

        for element in list:
            print(element)
        print("\n")


createSpiral(11)
