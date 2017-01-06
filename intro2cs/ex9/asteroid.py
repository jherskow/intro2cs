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
