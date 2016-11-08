##########################################################################
# FILE : math_print.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex0 2016-2017
# DESCRIPTION: Functions that print values using the math module.
##########################################################################
import math

def golden_ratio():
    print(2 * (math.cos(math.pi/5)))

def square_five():
    print(math.pow(5,2))

def hypotenuse():
    print(math.hypot(4,5))

def pi():
    print(math.pi)

def e():
    print(math.e)

def squares_area():
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2), math.pow(4, 2), math.pow(5, 2), math.pow(6, 2),
          math.pow(7, 2), math.pow(8, 2), math.pow(9, 2), math.pow(10, 2))
