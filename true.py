# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Nicole Grimaldos

# Student UT EID: ng23476

# Course Name: CS 313E

# Unique Number: 52230

import sys
import math

TOL = 0.01


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


class Triangle(object):
    # constructor

    def __init__(self, Point1, Point2, Point3):
        self.point1 = Point1
        self.point2 = Point2
        self.point3 = Point3

    # print string representation of Triangle
    def __str__(self):
        return 'Point1: (' + str(self.point1.x) + ', ' + str(self.point1.y) + '), Point2: (' + str(self.point2.x) + ', ' \
               + str(self.point2.y) + '), Point3: (' + str(self.point3.x) + ', ' + str(self.point3.y) + ')'

    # check congruence of Triangles with equality

    # returns whether or not the triangle is valid

    def is_triangle(self):
        if self.point1.dist(self.point2) + self.point2.dist(self.point3) > self.point3.dist(self.point1):
            if self.point3.dist(self.point1) + self.point2.dist(self.point3) > self.point1.dist(self.point2):
                if self.point3.dist(self.point1) + self.point1.dist(self.point2) > self.point2.dist(self.point3):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    # return the area of the triangle:

    def area(self):
        return abs([self.point1.x * (self.point2.y - self.point3.y) + self.point2.x * (
                    self.point3.y - self.point1.y) + self.point3.x * (self.point1.y - self.point2.y)] / 2)


######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)] * 2)]


def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA)
    print(triangleB)
    print(triangleA.area())
    print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)


if __name__ == "__main__":
    main()
