"""########################################################################
# FILE : helpers.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import math
import random
import copy

# ============ helper functions ===========================================

# ===== constants =====
HALF_CIRCLE = 180
PI = math.pi
CIRCLE = 360
MIN_SPEED = -5
MAX_SPEED = 5


# ===== Helper Functions =========

def deg_to_radian(degs):
    """converts degrees to radians"""
    return (degs * PI) / HALF_CIRCLE


def random_heading():
    """returns a random compass heading (int) """
    return random.randint(1, CIRCLE)


def random_speed():
    """returns a random [x,y] speed"""
    x = random.randint(MIN_SPEED, MAX_SPEED)
    y = random.randint(MIN_SPEED, MAX_SPEED)
    while x == 0 and y == 0:
        x = random.randint(MIN_SPEED, MAX_SPEED)
        y = random.randint(MIN_SPEED, MAX_SPEED)
    return [x, y]

# ===== Parent Class for space objects =========


class Movable:
    """
    Parent class designed to consolidate identical getters for
    classes: Asteroid, Ship and Torpedo.
    """

    def goto(self, pos):
        """
        Sends a movable object to a specified [x,y] position.
        :param pos: [x,y] list indicating a position on the board.
        """
        self._pos = pos

    def get_heading(self):
        """ returns space object's compass heading as an int"""
        return copy.copy(self._heading)

    def get_speed(self):
        """ :return: speed as [x,y] list"""
        return copy.copy(self._speed)

    def get_pos(self):
        """ :return: position coordinates as [x,y] list"""
        return copy.copy(self._pos)

    def get_x_pos(self):
        """ :return: x position coordinate as float"""
        return copy.copy(self._pos[0])

    def get_y_pos(self):
        """ :return: y position coordinate as float"""
        return copy.copy(self._pos[1])

    def get_x_speed(self):
        """  :return: x speed as float """
        return copy.copy(self._speed[0])

    def get_y_speed(self):
        """ :return: y speed as float"""
        return copy.copy(self._speed[1])

    def get_radius(self):
        """ :return: radius as int"""
        return copy.copy(self._radius)

    def get_size(self):
        """ :return: size as sub-class constant"""
        return copy.copy(self._size)
