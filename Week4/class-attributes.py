import random
from math import sqrt
import numpy as np


class Vector:
    """
    A simple class to hold a 3D points
    """

    def __init__(self, _x=0, _y=0, _z=0):
        """
        Constructor a vector with (x,y,z) values. (0,0,0) unless specified.
        :param _x: Initial x value. Default is 0.
        :param _y: Initial y value. Default is 0
        :param _z: Initial z value. Default is 0
        """
        self.x = _x
        self.y = _y
        self.z = _z

    def __str__(self):
        """
        Function overload to ensure that vector will print 'cleanly'
        :return: Printable string for vector
        """
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ">"


### Main program begins here... ###

# create two simple vectors
a = Vector(3, 1, -2)
b = Vector(9, 2, 4)

# treat the vectors as point as compute the distance between (should be 8.54)

distance = sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)
print("Distance between ", a, " and ", b, " is ", distance)

# treat vectors as vectors and compute the dot product (should be 21)
dot_product = (a.x * b.x) + (a.y * b.y) + (a.z * b.z)
print("Dot product between ", a, " and ", b, " is ", dot_product)

# generate two random vectors and perform the same operations
(x, y, z) = random.sample(range(10), 3)
v1 = Vector(x, y, z)

(x, y, z) = random.sample(range(10), 3)
v2 = Vector(x, y, z)

# treat the vectors as point as compute the distance between (check result by hand)
distance = sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2)
print("Distance between ", v1, " and ", v2, " is ", distance)

# treat vectors as vectors and compute the dot product (check result by hand)
dot_product = (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)
print("Dot product between ", v1, " and ", v2, " is ", dot_product)