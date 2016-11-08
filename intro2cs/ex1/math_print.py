##########################################################################
# FILE : math_print.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex0 2016-2017
# DESCRIPTION: Functions that print values using the math module.
##########################################################################
import math

def golden_ratio():
    """prints value of golden ratio"""
    print(2 * (math.cos(math.pi/5)))

def square_five():
    """prints value of 5^2 """
    print(math.pow(5,2))

def hypotenuse():
    """prints value hypotenuse for sides 4 and 5"""
    print(math.hypot(4,5))

def pi():
    """prints value of pi"""
    print(math.pi)

def e():
    """prints value of e"""
    print(math.e)

def squares_area():
    """prints float value of the squares of 1 through ten"""
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2), math.pow(4, 2), math.pow(5, 2), math.pow(6, 2),
          math.pow(7, 2), math.pow(8, 2), math.pow(9, 2), math.pow(10, 2))
