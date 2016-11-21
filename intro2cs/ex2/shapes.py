##########################################################################
# FILE : shapes.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A fun geometry tool.
##########################################################################
import math


def circle_area(radius):
    """Returns float area of circle with given radius"""
    area = radius ** 2 * (math.pi)
    return area


def rectangle_area(width, length):
    """Returns float area of square with given sides"""
    area = width * length
    return area


def trapeziod_area(top, bottom, height):
    """Returns float area of rectangle with specified properties"""
    area = ((top+bottom)/2) * height
    return area


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
        circle_area(float(input()))
    elif shape_choice == 2:     #rectangle
        area = rectangle_area(float(input()), float(input()))
    elif shape_choice == 3:     #trapeziod
        area = trapeziod_area(float(input()),
                              float(input()), float(input()))
    return area
