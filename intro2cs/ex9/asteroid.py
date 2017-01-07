"""########################################################################
# FILE : asteroid.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import helpers
import copy
import math

DEFAULT_SIZE = 3
DEFAULT_SPEED = helpers.random_speed()


class Asteroid:
    """
    An asteroid
    """
    # ===== Asteroid - class constants =====
    SIZE_L = 3
    SIZE_M = 2
    SIZE_S = 1
    SIZE_MODIFIER = 10
    SIZE_NORMALIZER = 5

    # ===== Asteroid - class methods =======

    def __init__(self, pos, size=DEFAULT_SIZE, speed=DEFAULT_SPEED):
        """
        Initialises a new asteroid.
        :param pos: [x,y] list representing cartesian coordinates.
        :param size: size of asteroid - default 3
        """
        self._size = size
        self._speed = speed
        self._pos = pos
        radius = size * Asteroid.SIZE_MODIFIER - Asteroid.SIZE_NORMALIZER
        self._radius = radius

    def goto(self, pos):
        """ docstring """
        self._pos = pos

    def has_intersection(self, obj):
        """ checks if asteroid has hit something"""
        x_diff = self.get_x_pos() - obj.get_x_pos()
        x_diff_pow = x_diff ** 2
        y_diff = self.get_y_pos() - obj.get_y_pos()
        y_diff_pow = y_diff ** 2
        distance = math.sqrt(x_diff_pow + y_diff_pow)
        if distance <= self._radius + obj.get_radius():
            return True
        else:
            return False

    def get_speed(self):
        return copy.copy(self._speed)

    def get_size(self):
        return copy.copy(self._size)

    def get_pos(self):
        return copy.copy(self._pos)

    def get_x_pos(self):
        return copy.copy(self._pos[0])

    def get_y_pos(self):
        return copy.copy(self._pos[1])

    def get_x_speed(self):
        return copy.copy(self._speed[0])

    def get_y_speed(self):
        return copy.copy(self._speed[1])

    def get_radius(self):
        return copy.copy(self._radius)