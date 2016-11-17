##########################################################################
# FILE : shapes.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A fun geometry tool.
##########################################################################
import math

def shape_area():
    """
    Calculates and returns the area of different shapes.
    The shape and its measurements are given by user input.
    """
    area = None
    shape_choice = input("Choose shape (1=circle, 2=rectangle,"
                         " 3=trapezoid): ")
    shape_choice = int(shape_choice)
    if shape_choice == 1:       #circle
        radius = float(input())
        area = radius**2*(math.pi)
    elif shape_choice == 2:     #rectangle
        width = float(input())
        length = float(input())
        area = width*length
    elif shape_choice == 3:     #trapeziod
        top = float(input())
        bottom = float(input())
        height = float(input())
        area = ( (top + bottom)/2 ) * height
    return area
