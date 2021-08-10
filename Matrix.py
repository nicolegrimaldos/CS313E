#  File: Matrix.py

#  Description: Determines if a square 2d list of 1s and 0s has some "symmetry" where the matrix is 
#               the same after one of the following operations: rotate clockwise 90 degrees, rotate 
#               counterclockwise 90 degrees, flip horizontally, or flip vertically

# Student Name: Nicole Grimaldos

# Student UT EID: ng23476

# Course Name: CS 313E

# Unique Number: 52230

import sys

# Prints your 2d list
# Can be used for debugging purposes
def print_arr(temp):
    mx = max((len(str(ele)) for sub in temp for ele in sub))
    for row in temp:
        print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))
    print()


# Input: matrix is a 2d square list of 1s and 0s
# Output: return True if a rotation by 90 degrees in either direction (clockwise/counterclockwise)
# or a horizontal/vertical flip results in the matrix being equal to itself.
# return False otherwise

def matrix_has_symmetry(matrix):
    new = rotateForward(matrix)
    t = True
    z = 0
    b = 0
    len1 = 0
    for i in matrix:
        len1 += 1
    for i in range(len1):
        for x in range(len1):
            if matrix[i][x] != new[i][x]:
                return False
                t = False
            z += 1
        b += 1
    if t:
        return True



def rotateForward(matrix):
    for row in range(len(matrix) // 2):
        for col in range(row, len(matrix) - row - 1):
            temp = matrix[row][col]
            matrix[row][col] = matrix[len(matrix) - 1 - col][row]
            matrix[len(matrix) - 1 - col][row] = matrix[len(matrix) - 1 - row][len(matrix) - 1 - col]
            matrix[len(matrix) - 1 - row][len(matrix) - 1 - col] = matrix[col][len(matrix) - 1 - row]
            matrix[col][len(matrix) - 1 - row] = temp
    return matrix



def main(): 
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to matrix_has_symmetry()
    result = matrix_has_symmetry(matrix)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()