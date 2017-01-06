"""########################################################################
# FILE : asteroid.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import helpers
from screen import Screen

ASTEROID_SIZE = 3


class Asteroid:
    """
    An asteroid
    """
    # ===== Asteroid - class constants =====

    # ===== Asteroid - class methods =======

    def __init__(self, pos):
        """
        Initialize a new asteroid
        """
        self._size = ASTEROID_SIZE
        self._speed = helpers.random_speed()
        self._pos = pos  # (x,y) tuple

    def goto(self, pos):
        """ docstring """
        self._pos = pos

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